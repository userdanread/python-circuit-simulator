import tkinter as tk
from logicGate import *

def setInp1(val):
    inp1 = val
    print(inp1)

def setInp2(val):
    inp2 = val
    print(inp2)


main = tk.Tk()
main.geometry("500x500")
main.title("Circuit Simulator")
main.resizable(0, 0)
main.configure(background="black")



AND1 = logicGate("AND")

output = AND1.getOutput(1,0)
print(output)
output = AND1.getOutput(1,1)
print(output)


