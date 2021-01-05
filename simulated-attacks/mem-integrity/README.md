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
  * Run the Python script that modifies the memory  
    Use the found PID in the following command:  
    python3 mem_attack.py 21566 0x64ed88 0 0 0 0 0  
    21566 is the PID of the process we want to attack  
    0x64ed88 is the address in the heap of the buffer we want to overwrite.  
    This information is printed from the C library called by the line_follower_clib.py script  
    0 0 0 0 0 are the values for the 5 sensors we want to overwrite  
  * Observe that the host application displays the new sensor readings and the car is not able to follow the line while we keep the attack going. 
    Once the attack stops the car is able to continue to follow the line. 
    
   
