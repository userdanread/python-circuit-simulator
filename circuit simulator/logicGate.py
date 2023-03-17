def AND(inp1, inp2):
    if inp1 == 1 and inp2 == 1:
        return 1
    return 0

def OR(inp1, inp2):
    if inp1 == 1 or inp2 == 1:
        return 1
    return 0

def NOT(inp1):
    if inp1 == 1:
        return 0
    return 1

def NAND(inp1, inp2):
    if inp1 == 1 and inp2 == 1:
        return 0
    return 1

def NOR(inp1, inp2):
    if inp1 == 0 or inp2 == 0:
        return 1
    return 0

def XOR(inp1, inp2):
    if (inp1 == 1 and inp2 == 0) or (inp1 == 0 and inp2 == 1):
        return 1
    return 0

class logicGate:
    def __init__(self, name):
        self.name = name
        self.gates = {
            "AND": AND,
            "OR" : OR,
            "NOT" : NOT,
            "NAND" : NAND,
            "NOR" : NOR,
            "XOR" : XOR
        }

    def getOutput(self, inp1, inp2=None):
        gate_func = self.gates.get(self.name)
        if gate_func:
            if inp2 is None:
                return gate_func(inp1)
            else:
                return gate_func(inp1, inp2)
        else:
            raise ValueError("Invalid gate name")




        
        


