import subprocess
import tkinter as tk

servers = {
    "VXSQL": "172.16.1.150",
    "VXDIRSRV": "172.16.1.151",
    "VXREPORT": "172.16.1.153",
    "VXSERVNO": "172.16.1.154",
    "VXCATI1": "172.16.1.156",
    "VXCATI2": "172.16.1.157",
    "VXDLR1": "172.16.1.158",
    "VXOADMIN": "172.16.1.160",
    "VXONLINE": "172.16.1.161",
    "VXTCPA": "172.16.1.163",
    "VXDIAL": "172.16.1.165"
}

def ping_location(location):
    try:
        subprocess.check_call(f'ping -n 1 -w 1 {location}', stdout=subprocess.DEVNULL)
        return True
    except Exception as e:
        return False

def update_status():
    for i, (server, ip) in enumerate(servers.items()):
        status = ping_location(ip)  # Ping IP address
        color = 'green' if status else 'red'
        labels[i].config(text=server, bg=color)

    root.after(5000, update_status)  # Check status every 5 seconds

root = tk.Tk()
root.title('Server Status')

labels = []
for server in servers:
    label = tk.Label(root, text=server, width=20)
    label.pack()
    labels.append(label)

update_status()

root.mainloop()

