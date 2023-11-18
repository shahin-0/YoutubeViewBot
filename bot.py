import requests
import threading
import time
import random
import tkinter as tk
from tkinter import messagebox

def run():
    global running
    running = True
    while running:
        try:
            proxy = get_proxy()
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
            requests.get(url, proxies={"http": proxy, "https": proxy}, headers=headers, timeout=5)
            time.sleep(random.randint(15, 30))
        except:
            pass

def start():
    global url
    global t
    global running
    if url_entry.get() == '':
        messagebox.showerror('Error', 'Please enter a video URL')
        return
    url = url_entry.get()
    t = threading.Thread(target=run)
    t.start()
    start_button.config(state='disabled')
    stop_button.config(state='normal')
    running = True

def stop():
    global running
    running = False
    t.join()
    start_button.config(state='normal')
    stop_button.config(state='disabled')

def get_proxy():
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all')
    proxies = r.content.decode().split('\r\n')
    return random.choice(proxies)

root = tk.Tk()
root.title("YouTube View Bot")
root.geometry('250x100')
root.resizable(False, False)

url_label = tk.Label(root, text="Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

start_button = tk.Button(root, text="Start", command=start)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop, state='disabled')
stop_button.pack()

root.mainloop()