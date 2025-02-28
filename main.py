import csv
from tkinter import Tk, Frame, Label

root = Tk()
root.title("Ramais v1.0.0")
root.resizable(False, False)
root.attributes('-topmost', True)

frame = Frame(root)
frame.pack()

try:
    with open('list.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
except FileNotFoundError:
    data = []

if not data:
    data = [["#BDBAB5", "100", "Recepção"]]
    with open('list.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

for row in data:
    color, number, place = row
    number_label = Label(frame, text=number, bg=color, width=10, relief="solid", borderwidth=1)
    number_label.grid(row=data.index(row), column=0)
    
    place_label = Label(frame, text=place, width=24, relief="solid", borderwidth=1)
    place_label.grid(row=data.index(row), column=1)

last_label = Label(frame, text=" * 0 (puxar ligação)", width=34, relief="solid", borderwidth=0, pady=4)
last_label.grid(row=len(data), column=0, columnspan=2)

root.mainloop()
