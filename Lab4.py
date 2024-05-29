import os
from dynamixel_workbench_msgs.srv import DynamixelCommand
from sensor_msgs.msg import JointState
import rospy
import numpy as np
from cmath import pi

author = "Juan Camilo Aguilar"
credits = ["Juan Camilo Aguilar"]
email = "jaguilarc@unal.edu.co"
status = "Test"

positions_degrees = [0,0,0,0,0]

points = {0:(0,0,0,0,0),
          1:(25,25,20,-20,0),
          2:(-35,35,-30,30,0),
          3:(85,-20,55,25,0),
          4:(80,-35,55,-45,0)}

torques = (800,600,600,500,500)

next_pos = points[0]  


def listener():
    rospy.init_node('joint_listener', anonymous = True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)

def deg2motor(deg):
    motor = round((1024/300)*deg + 512)
    if motor > 1023: 
        print('Check the joint configuration data')
        return 1023
    elif motor < 0: 
        print('Check the joint configuration data')
        return 0
    else: 
        return motor

def callback(data):
    global positions_degrees
    positions_degrees = np.round(np.multiply(data.position, 180/pi),3)
    

    
def ErrorPrint():
    

    art = ["Waist           |",
           "Shoulder        |",
           " Elbow          |",
           " Wrist          |",
           "Gripper         |"]

    print( "                |      Position      |      objective      |      Error      ")
    


    for i in range(5):
          print()
          
          print(f"{art[i]}      {positions_degrees[i]}°                {next_pos[i]}°                {np.round(next_pos[i] - positions_degrees[i],3)}°", end= " ")




          
    print()

     

def jointCommand(command, id_num, addr_name, value, time):
    #rospy.init_node('joint_node', anonymous=False)
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:   
        print(str(exc))

def joint(id, position):
    jointCommand('', id, 'Goal_Position', position, 1)

def movement(position):
    os.system('clear')
    global next_pos
    next_pos = points[position]
    
    if position == 0:
        position = "home"
        
    print(f"Next Position {position}: {next_pos} \n")
    
    
    for i in range(5):
        print(f"Moving joint: {i+1} \n\n")
        joint(i+1, deg2motor(next_pos[i]))
        
   
    
def initial_config():
    for i in range(5):
        jointCommand('', i+1, 'Torque_Limit', torques[i], 0)
    for i in range(5):
        joint(i+1, deg2motor(0))
    return


def main():
    os.system('clear')
    try: 
        listener()
        initial_config()
        os.system('clear')
        while True:
            print("Welcome to the Robot Control System \n\n")
            print("By Juan Camilo Aguilar Coronado\n\n")

            print("Select a position from the menu below: \n\n")
            print("Home Position:   0")
            print("Position 1:      1")
            print("Position 2:      2")
            print("Position 3:      3\n")
            print("Position 4:      4\n")
            
            print("Exit Program:      E \n")
            

            choise = str(input("Select the Position of Your Preference: "))
            
            if (choise == "e" or choise =="E"):
                for i in range(5):
                    joint(i+1, deg2motor(0))
                break
                
            
            try:
                
                
                num_choise = int(choise)
                
                if (num_choise > 4  or num_choise < 0):
                    print("Choose a valid position")
                    input()
                else:
                   
                    movement(num_choise)
                    ErrorPrint()
                    input()     
            except:
                print("Your option must be a number")
                input()
            os.system('clear')
    except:
        print('Not posible connect to robot')
        pass

# Main function
if __name__ == '__main__':
    main()
