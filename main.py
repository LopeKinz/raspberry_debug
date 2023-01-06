import tkinter as tk
import subprocess
import platform
import psutil
def get_system_info():
    cpu_usage = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    info = f'CPU Usage: {cpu_usage}%\nVirtual Memory: {virtual_memory.used / (1024 ** 3):.2f} GB / {virtual_memory.total / (1024 ** 3):.2f} GB ({virtual_memory.percent}%)\nDisk Usage: {disk_usage.used / (1024 ** 3):.2f} GB / {disk_usage.total / (1024 ** 3):.2f} GB ({disk_usage.percent}%)'
    return info

def get_cpu_usage():
    return psutil.cpu_percent()

def get_disk_space():
    disk = psutil.disk_usage('/')
    return f'{disk.used}/{disk.total} GB'

def get_ram_usage():
    ram = psutil.virtual_memory()
    return f'{ram.used}/{ram.total} GB'

def check_wifi_bluetooth():
    wifi = "Connected" if psutil.sensors_battery().power_plugged else "Not Connected"
    bluetooth = "Connected" if psutil.sensors_battery().power_plugged else "Not Connected"
    return f'Wifi: {wifi}, Bluetooth: {bluetooth}'

def get_session_time():
    return psutil.users()[0].session

window = tk.Tk()
window.title("System Information")

cpu_label = tk.Label(master=window, text=f'CPU Usage: {get_cpu_usage()}%')
disk_label = tk.Label(master=window, text=f'Disk Space: {get_disk_space()}')
ram_label = tk.Label(master=window, text=f'RAM Usage: {get_ram_usage()}')
wifi_bluetooth_label = tk.Label(master=window, text=f'{check_wifi_bluetooth()}')
session_label = tk.Label(master=window, text=f'Session Time: {get_session_time()}')


cpu_label.pack()
disk_label.pack()
ram_label.pack()
wifi_bluetooth_label.pack()
session_label.pack()

window.mainloop()

root.mainloop()
