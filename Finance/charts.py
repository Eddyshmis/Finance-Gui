import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

test_x = [1,2,3,5]
test_y = [1,2,3,4]

root = tk.Tk()
root.title("data charts")
root.geometry('400x400')

def graph():
    plt.plot(test_y,test_x)
    plt.show()

graph_btn = tk.Button(root, text="graph button", command=graph)
graph_btn.grid(row=1, column=0, padx=10, pady=10)
root.mainloop()
