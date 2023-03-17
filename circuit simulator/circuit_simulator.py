import tkinter as tk
from logicGate import *

def onMouseClick(event):
    mouse_x =0
    mouse_y =0
    mouse_x = event.x
    mouse_y = event.y
    canvas.unbind("<Button-1>")
    canvas.unbind("<Motion>")
    #print("Mouse Position = {}, {}".format(mouse_x, mouse_y))

    return mouse_x, mouse_y

def spawnGate(mouse_x, mouse_y, gateName):
    x = mouse_x
    y = mouse_y
    print("Gate location: =  x: {}  y: {}".format(x,y))
    print("Gate type: {}".format(gateName))

def loadGate(gateName):
    canvas.bind("<Motion>", lambda event: print("Mouse x: {}  Mouse y: {}".format(event.x,event.y)))
    canvas.bind("<Button-1>", lambda event: spawnGate(*onMouseClick(event), gateName))  # "*" - unloads the function (ie. takes its outputs directly from the function


main = tk.Tk()
main.geometry("1000x600")
main.title("Circuit Simulator")
main.resizable(0, 0)
main.configure(background="black")


canvas = tk.Canvas(main, height=500, width=800)
canvas.place(x=160, y=40)

butCreateGate_AND = tk.Button(main, text="Input", font=10, height=1, command=lambda:loadGate("AND"))
butCreateGate_AND.place(x=10, y=550)


main.mainloop()


AND1 = logicGate("AND")

output = AND1.getOutput(1,0)
print(output)
output = AND1.getOutput(1,1)
print(output)


