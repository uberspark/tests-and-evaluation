# Memory Intrusion Example Using the /proc File System

## Contents and Modifications
This example was downloaded from this location:  
 https://medium.com/@holdengrissett/linux-101-how-to-hack-your-process-memory-2514a3d0778d  

The code contains host_app.c which was not modified and mem_attack.py file,  
 which had to be modified, because of a run time error with Python 3.

## Steps for running the simple test

  * Build the host application to be attacked:  
    make  
  * Run the host application:  
    python3 line_follower_clib.py  
  * Find the PID of the host application  
    ps -aux | grep python3  

    pi@raspberrypi:~ $ ps -aux | grep python3  
    root      2961  0.1  0.3   6184  2960 pts/0    S+   19:14   0:00 sudo python3 line_follower_clib.py  
    root      **2965**  7.8  0.8  12668  7948 pts/0    S+   19:14   0:01 python3 line_follower_clib.py  
    pi        3123  0.0  0.2   4276  2004 pts/1    S+   19:14   0:00 grep --color=auto python3  

  * Run the Python script that modifies the memory  
    Use the PID form the second printed line, **2965** in the example above.  
    Use the found PID in the following command:  
     
    *python3 mem_attack.py 2965 0x7689e200 0 0 0 0 0*  
    
    21566 is the PID of the process we want to attack  
    **0x7689e200** is the address in the heap of the buffer we want to overwrite.  
    read_digital() :: digital_list address : **0x7689e200**  
    This information is printed from the C library called by the line_follower_clib.py script  
    0 0 0 0 0 are the values for the 5 sensors we want to overwrite  
  * Observe that the host application displays the new sensor readings and the car is not able to follow the line while we keep the attack going. 
    Once the attack stops the car is able to continue to follow the line. 
    
   
