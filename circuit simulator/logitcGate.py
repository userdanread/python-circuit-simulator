class logitGate(object):
    gates = {
    "AND": AND,
    "OR" : OR,
    "NOT" : 3,
    "NAND" : 4,
    "NOR" : 5,
    "XOR" : 6
    }

    def __init__(inp1, inp2, name):
        self.inp1 = inp1
        self.inp2 = inp2
        self.name = name

        gate = gates.get(name)

    def AND():
        inp1 = __init__.inp1
        inp2 = __init__.inp2

        if inp1 == 1 and inp2 == 1:
            return 1
        return 0

    def OR():
        inp1 = __init__.inp1
        inp2 = __init__.inp2

        if inp1 == 1 or inp2 == 1:
            return 1
        return 0

    def NOR():
        inp1 = __init__.inp1
        inp2 = __init__.inp2

        if inp1 == 0 or inp2 == 0:
            return 1
        return 0



            





        
        


