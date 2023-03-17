import tkinter as tk
from logicGate import *

#mouse_x = 0
#mouse_y = 0
def spawnAND(gatex, gatey):
    butTestSpawn = tk.Button(main, text="AND!!", font=10)
    butTestSpawn.place(x=gatex,y=gatey)


def trackMouse(name):
    canvas.bind("<Motion>", lambda event: print("Mouse position: ({}, {})".format(event.x, event.y)))  # tracks the mouse over the canvas
    canvas.bind("<Button-1>", lambda event: placeGate(name))

def spawnGate(type):
    trackMouse(type)

def placeGate(event, type):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y
    canvas.unbind("<Motion>")
    print("Your mouse is at location: {} {} ".format(mouse_x,mouse_y))
    gates = {                   # acts like a switch-case
            "AND": lambda: spawnAND(mouse_x, mouse_y),
            "OR" : 1,
            "NOT" : 1,
            "NAND" : 1,
            "NOR" : 1,
            "XOR" : 1
    }

    createFunc = gates.get(type)

    createFunc()


# Menu buttons


main = tk.Tk()
main.geometry("1000x600")
main.title("Circuit Simulator")
main.resizable(0, 0)
main.configure(background="black")


canvas = tk.Canvas(main, height=500, width=800)
canvas.place(x=160, y=40)

butCreateGate_AND = tk.Button(main, text="Input", font=10, height=1, command=lambda:spawnGate("AND"))
butCreateGate_AND.place(x=10, y=550)


main.mainloop()


AND1 = logicGate("AND")

output = AND1.getOutput(1,0)
print(output)
output = AND1.getOutput(1,1)
print(output)


