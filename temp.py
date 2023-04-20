import os
import time
from gpiozero import CPUTemperature
while True:
  cpu = CPUTemperature()
  print(cpu.temperature)
  time.sleep(1000)
  os.system("clear")
  
