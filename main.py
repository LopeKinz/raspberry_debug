import tkinter as tk
import platform
import psutil

def get_cpu_usage():
    return psutil.cpu_percent()

def get_disk_space():
    disk = psutil.disk_usage('/')
    return f'{disk.used}/{disk.total} GB'

def get_ram_usage():
    ram = psutil.virtual_memory()
    return f'{ram.used}/{ram.total} GB'

#def check_wifi_bluetooth():
   # wifi = "Connected" if psutil.sensors_battery().power_plugged else "Not Connected"
    #bluetooth = "Connected" if psutil.sensors_battery().power_plugged else "Not Connected"
   # return f'Wifi: {wifi}, Bluetooth: {bluetooth}'

def get_session_time():
    return psutil.users()[0].session
try:
    window = tk.Tk()
    window.title("System Information")

    cpu_label = tk.Label(master=window, text=f'CPU Usage: {get_cpu_usage()}%')
    disk_label = tk.Label(master=window, text=f'Disk Space: {get_disk_space()}')
    ram_label = tk.Label(master=window, text=f'RAM Usage: {get_ram_usage()}')
    #wifi_bluetooth_label = tk.Label(master=window, text=f'{check_wifi_bluetooth()}') #funtioniert nicht da der raspberry pi keine batterie hat (ka warum wlan und bluetooth einen zusammenhang mit batterie haben)
    session_label = tk.Label(master=window, text=f'Session Time: {get_session_time()}')


    cpu_label.pack()
    disk_label.pack()
    ram_label.pack()
    wifi_bluetooth_label.pack()
    session_label.pack()

    window.mainloop()
except:
    print("System Information")
    print("__________________")
    print(f'CPU Usage: {get_cpu_usage()}%')
    print(f'Disk Space: {get_disk_space()}')
    print(f'RAM Usage: {get_ram_usage()}')
    print(f'Session Time: {get_session_time()}')
    print("__________________")

