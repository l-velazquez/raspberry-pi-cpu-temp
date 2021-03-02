
import time
from gpiozero import CPUTemperature
import os

# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))
    
cpu = CPUTemperature()

while True:
        today = time.strftime("%d/%m/%Y")
        t = time.strftime("%H:%M:%S")
        F = round((cpu.temperature * 9/5) + 32,1)
        C = round(cpu.temperature,1)
        usage = getCPUuse()
        print()
        print("-"*30)
        print(today+" "+t) 
        print("-"*30)
        print("Temp",F,"F ")
        print("Temp",C,"C")
        print("CPU usage", usage,"%")
        time.sleep(1)
