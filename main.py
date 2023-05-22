from math import sqrt

class QuantumBrainfuck():

    def __init__(self,size=10):
        self.__one = [0,1]
        self.__zero = [1,0]
        self.__tape = [self.__zero] * size
        self.__pointer1ind = 0
        self.__pointer2ind = 0
        self.__pointer1 = self.__tape[self.__pointer1ind]
        self.__pointer2 = self.__tape[self.__pointer2ind]
        self.__loop = [False,0]
        self.__main()

    def __main(self):
        while True:
            command = input("> ")
            command = command.split(" ")
            print("*************BEFORE*****************")
            print(self.__tape)
            self.__out()
            print("************************************")
            for command in command:
                self.__run(command)
            print("*************AFTER*****************")
            print(self.__tape)
            self.__out()
            print("***********************************")

    def __run(self,command:str):
        commands = ["H","Z","X","T","C","s1","s0"]
        operators = [">","<","2>","2<"]
        if command not in operators:
            command = command.upper()
        match command:
            case "s1": self.__set(1)
            case "s0": self.__set(0)
            case "H": self.__hadamard()
            case "T": self.__tensor()
            case "X": self.__not()
            case "Z": self.__z()
            case "C": self.__cnot()
            case ">": self.__move(1,">")
            case "<": self.__move(1,"<")
            case "2>": self.__move(2, ">")
            case "2<": self.__move(2, "<")

    def __set(self,val:int):
        if val == 1:
            self.__pointer1 = self.__one
        else:
            self.__pointer1 = self.__zero

    def __out(self):
        string1 = "("+ (str(self.__pointer1).strip("]")).strip("[") + "),"
        string2 = "(" + (str(self.__pointer2).strip("]")).strip("[") + "),"
        print("Pointer 1 (value, index):",string1,self.__pointer1ind)
        print("Pointer 2 (value, index):",string2,self.__pointer2ind)

    def __hadamard(self):
        HADAMARD = [[1 / sqrt(2), 1 / sqrt(2)],
                    [1 / sqrt(2), -1 / sqrt(2)]]
        result = [0] * 2
        for i in range(2):
            total = 0
            for j in range(2):
                total += HADAMARD[i][j] * self.__pointer1[j]
                result[i] = total
        self.__pointer1 = result

    def __tensor(self):
        size = len(self.__pointer1) * len(self.__pointer2)
        tensorprod = [0] * size
        i = -1
        for count,element in enumerate(self.__pointer1):
            for count2,element2 in enumerate(self.__pointer2):
                i += 1
                tensorprod[i] = element * element2
        self.__pointer1 = tensorprod

    def __move(self,pointer:int,direction:str):
        if pointer == 1:
            if self.__pointer1ind != 0:
                match direction:
                    case ">": self.__pointer1ind += 1
                    case "<": self.__pointer1ind -= 1
                    case _: pass
            else:
                match direction:
                    case ">": self.__pointer1ind += 1
                    case _: pass
        else:
            if self.__pointer2ind != 0:
                match direction:
                    case ">": self.__pointer2ind += 1
                    case "<": self.__pointer2ind -= 1
                    case _: pass
            else:
                match direction:
                    case ">": self.__pointer2ind += 1
                    case _: pass


    def __not(self):
        if len(self.__pointer1) != 2:
            pass
        else:
            if all((x == 1 or x == 0) for x in self.__pointer1):
                if self.__pointer1 == self.__one:
                    self.__pointer1 = self.__zero
                else:
                    self.__pointer1 = self.__one
            else:
                pass

    def __cnot(self):
        CNOT = [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]]
        result = [0] * 4
        self.__tensor()
        for i in range(4):
            total = 0
            for j in range(4):
                total += CNOT[i][j] * self.__pointer1[j]
                result[i] = total
        self.__pointer1 = result

    def __z(self):
        z = [[1, 0],
             [0, -1]]
        result = [0] * 2
        for i in range(2):
            total = 0
            for j in range(2):
                total += z[i][j] * self.__pointer1[j]
                result[i] = total
        self.__pointer1 = total

    def __setitem__(self, key:int, value:list):
        key = int(key)
        if key > len(self.__tape):
            for i in range(key-len(self.__tape)):
                self.__tape.append(self.__zero)
        self.__tape[key] = value

    def __getitem__(self, item:int):
        item = int(item)
        if item > len(self.__tape):
            for i in range(key-len(self.__tape)):
                self.__tape.append(self.__zero)
        return self.__tape[item]

    def __add(self):
        pass

    def __repr__(self) -> str:
        return str(self.__tape)

a = QuantumBrainfuck()
