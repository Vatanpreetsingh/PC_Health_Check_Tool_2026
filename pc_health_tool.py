import os
import platform
import psutil
import tempfile
from send2trash import send2trash

def disk_cleanup():
    print("\nRunning Disk Cleanup...")
    temp_dir = tempfile.gettempdir()
    deleted = 0

    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                send2trash(file_path)
                deleted += 1
            except:
                pass

    print(f"Disk Cleanup Complete. Temp files removed: {deleted}\n")

def system_information():
    print("\nSystem Information")
    print("------------------")
    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"Computer Name    : {platform.node()}")
    print(f"Processor        : {platform.processor()}")
    print(f"Architecture     : {platform.machine()}")
    print(f"Total RAM        : {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n")

def cpu_ram_usage():
    print("\nLive CPU & RAM Usage")
    print("-------------------")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    print(f"CPU Usage : {cpu}%")
    print(f"RAM Usage : {ram}%")

    if cpu > 80 or ram > 80:
        print("⚠ Warning: High system usage detected!\n")
    else:
        print("System running normally.\n")

def menu():
    while True:
        print("====================================")
        print(" PC HEALTH CHECK & IT SUPPORT TOOL ")
        print("====================================")
        print("1. Disk Cleanup (Temporary Files)")
        print("2. System Information")
        print("3. CPU & RAM Usage")
        print("4. Exit")
        print("====================================")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            disk_cleanup()
        elif choice == "2":
            system_information()
        elif choice == "3":
            cpu_ram_usage()
        elif choice == "4":
            print("\nExiting tool. Thank you!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

menu()
