import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Reloj")

clock_label = tk.Label(root, font=('calibri', 40, 'bold'), bg='white')
clock_label.pack(pady=20)

update_clock()

root.mainloop()
