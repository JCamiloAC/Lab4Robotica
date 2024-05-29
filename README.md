# Laboratorio 4 Robotica- Robot Phantom X Pincher
Presentado Por: Juan Camilo Aguilar Coronado
# Objetivos
Crear todos los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom X Pincher.

• Manipular los tópicos de estado y comando para todos los Joint Controllers del robot Phantom X Pincher.

• Manipular los servicios para todos los Joint Controllers del robot Phantom X Pincher.

• Conectar el robot Phantom X Pincher con MATLAB o Python usando ROS.

# Requisitos:
• Ubuntu versión 20.xx preferible 20.04 LTS con ROS.

• Espacio de trabajo para catkin correctamente configurado.

• Paquetes de Dynamixel Workbench. https://github.com/fegonzalez7/rob_unal_clase3

• Paquete del robot Phantom X: https://github.com/felipeg17/px_robot.

• Python o MATLAB 2015b o superior instalado en el equipo.

• Robotics toolbox de Mathworks (Disponible desde la versión 2015 en adelante).

• Toolbox de robótica de Peter Corke.

• Un (1) manipulador Phantom X Pincher con su base en madera.

# Evidencia de Funcionamiento:

https://youtu.be/7U7HsjwnKro

# Desarrollo
# Parámetros DH:

Se hallaron los parámetros Denavit-Hartenberg del mecanismo apoyandose del diagrama, este se colocó de esta manera debido a que los puntos en los cuales las articulaciones no estan desplazadas (el puntio al que llegan cuando se les indica que vayan a 0 en cada articulación) resulta en una pose completamente extendida en vertical.

![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/DHDiagram.png)

Despues de contar con este, se utilizó la función SerialLink junto con los parámetros hallados para generar una representación del robot que pudiera dar claridad sobre la pose, sobretodo la pose del efector final. Tambien se hallo la Matriz de transformación homogenea que relaciona el; sistema coordenado cartesiano absoluto o global con el sistema del efector final TCP.

Los parámetros DH son los siguientes:

![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/DH.png)

# Código:

Para el programa y poder garantizar la funcionalidad del código se utilizaron las siguientes librerías:
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Libraries.png)

Y se implementaron las funciones siguientes funciones encontradas en los repositorios guia:
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Listener.jpg)
Para el Caso de Listener se borró la función Spin que se encontraba al final para asegurar la comunicación continua con el robot. Para el caso de la función CallBack, se cambió completamente para que regresara los datos que la función listener entregaba en el formato necesario, en este caso cambiando la lectura de radianes a grados y ajustando las cifras decimales.
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/CallBack.jpg)
Finalmente la función JointCommand se dejó exactamente igual.
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/JointCommand.jpg)
Como la mayoria de las veces que se llama la fuinción jointCommand es para realizar un movimiento, se creo la función joint para resumir este proceso, esta asume el tipode comando y de información que va a recibir, así como el tiempo en que tendrá que ejecutarla, dejando a elección solamente la articulación a elegir, y la posición que se quiere para esta.
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/jointResumido.jpg)

Adicionalmente se implementó una función para que tomara los valores de los ángulos que se quieren enviar al robot, dados en grados, y los transformara en una escala que comprendiera este robot, es decir, mapearlo a un rango de valores entre 0 y 1024 que este dividido en 300 trozos y con el 0 ubicado en 512.
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/deg2motor.jpg)

Se implementó una función que moviera que ordenara mover todas las articulaciones del robot cuando se solicitara alcanzar la pose deseada, esta consta de una asignación de los puntos que corresponden a la pose como objetivo, y crea un bucle que mueve cada una de las articulaciones por separado, durante su ejecución.
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/MovementFunction.jpg)

También se implementó la función ErrorPrint, que indica la posición del robot respecto a la posición ideal fijada como objetivo, mostrando la posición real del robot, la posición objetivo, y el error que existe entre ambas:

![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/ErrorPrint.jpg)

Finalmente se cuenta con el ciclo main, que hace una serie de evaluaciones de las entradas que se indican al programa para no entrar en errores, y despues ejecuta cada parte del programa, mientras va limpiando la consola.
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/MainFunction.jpg)


# Matlab

Utilizando MATLAB, se pudieron hallar las poses objetivo, estas en el archivo python se decidieron guardar en un diccionario y sus valores corresponden al ángulo de cada articulación, la priomera posición es un 0 debido a que esta es la posición de home:
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Puntos.png)

Las poses son las siguiente:
HOME
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/HomeMatlab.png)
POSE 1 
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose1Matlab.png)
POSE 2
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose2Matlab.png)
POSE 3
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose3Matlab.png)
POSE 4 
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose4Matlab.png)

#Robot

Utilizando el Script de python descrito anteriormente se obtuvieron los siguientes resultados:

En primer lugar las poses son las siguientes:

HOME
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/HomeRobot.jpg)
POSE 1 
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose1Robot.jpg)
POSE 2
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose2Robot.jpg)
POSE 3
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose3Robot.jpg)
POSE 4 
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Pose4Robot.jpg)

Ahora se puede ver como está configurada la interfaz:
Entrada de Interfaz
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Entrada.png)
Datos pose 1
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Posicion1Medidas.png)

Datos pose 2
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Posicion2Medidas.png)

Datos pose 3
![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/imagenes/Posicion3Medidas.png)

Comparando los resultados obtenidos en MATLAB y los obtenidos utilizando el robot real, se puede ver que el movimineto es el deseado, o por lo menos similar, lo cual se puede ver corroborado por los datos mostrados en la interfaz.











![](https://github.com/JCamiloAC/Lab4Robotica/blob/main/.png)

