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
    ./host_app "Good, safe variable"  
  * Find the PID of the host application  
    ps -aux | grep host_app  
  * Run the Python script that modifies the memory  
    Use the found PID in the following command:  
    sudo ./mem_attack.py PID "Good, safe variable" "Boom, Hacked!"  
  * Observe that the host application displays the new string in its memory location  
    [84] Good, safe variable - addr: 0x5555555592a0  
    [85] Boom, Hacked! - addr: 0x5555555592a0  