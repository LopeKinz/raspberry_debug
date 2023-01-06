import tkinter as tk
import psutil

def get_system_info():
    cpu_usage = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    info = f'CPU Usage: {cpu_usage}%\nVirtual Memory: {virtual_memory.used / (1024 ** 3):.2f} GB / {virtual_memory.total / (1024 ** 3):.2f} GB ({virtual_memory.percent}%)\nDisk Usage: {disk_usage.used / (1024 ** 3):.2f} GB / {disk_usage.total / (1024 ** 3):.2f} GB ({disk_usage.percent}%)'
    return info

root = tk.Tk()
root.title('System Info')

label = tk.Label(root, text=get_system_info())
label.pack()

root.mainloop()
