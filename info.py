import platform
import psutil

# Display information about the operating system
print(f"Operating System: {platform.system()} {platform.release()}")

# Display information about the CPU
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()
print(f"CPU cores: {cpu_count}")
print(f"CPU frequency: {cpu_freq.current:.2f} MHz")

# Display information about the memory
memory_info = psutil.virtual_memory()
print(f"Total memory: {memory_info.total // (1024**2)} MB")
print(f"Available memory: {memory_info.available // (1024**2)} MB")

# Display information about the disk
disk_info = psutil.disk_usage("/")
print(f"Total disk space: {disk_info.total // (1024**3)} GB")
print(f"Used disk space: {disk_info.used // (1024**3)} GB")


print("Running tasks:")
for process in psutil.process_iter():
    print(f"{process.name()} (ID: {process.pid})")
