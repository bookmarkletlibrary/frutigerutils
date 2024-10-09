import os
import tkinter as tk
import requests
import subprocess
import webbrowser

def create_bat_file():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    bat_content = r'cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%1""'
    with open(os.path.join(desktop, "notauacbypass.bat"), "w") as bat_file:
        bat_file.write(bat_content)

def download_and_run_opera():
    url = 'https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=(direct)&utm_medium=doc&utm_campaign=(direct)&http_referrer=missing&utm_site=opera_com&&utm_lastpage=opera.com/'
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop, "OperaSetup.exe")
    
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    subprocess.Popen([file_path], shell=True)

def open_url():
    webbrowser.open('https://64.227.120.231/')

window = tk.Tk()
window.title("Frutigers School Utils")

button1 = tk.Button(window, text="UAC Bypasser V1", command=create_bat_file)
button1.pack(pady=20)
label1 = tk.Label(window, text="This bypasses User Account Control, drag the program you want to run or install over it and go crazy!")
label1.pack(pady=5)

button2 = tk.Button(window, text="Download and Run Opera", command=download_and_run_opera)
button2.pack(pady=20)
label2 = tk.Label(window, text="This browser completely bypasses all blockers. If this doesn't work, Contact me at solarmenugtag@gmail.com")
label2.pack(pady=5)

button3 = tk.Button(window, text="Open URL", command=open_url)
button3.pack(pady=20)
label3 = tk.Label(window, text="This will open CroxyProxy, the best proxy. It allows you to go to any website, completely unrestricted!")
label3.pack(pady=5)

note_label = tk.Label(window, text="LS / BP soon!")
note_label.pack(pady=20)

window.mainloop()
