def q1():
    name = input("What is your name?")
    print(f"Hello {name}")

    id = int(input("What is your Student ID?"))
    print(f"Your ID is {id}")

def q2():
    var1 = float(input("var1 : "))
    var2 = float(input("var2 : "))

    sum = var1 + var2
    diff = (var1 - var2)
    prod = var1 * var2

    print(f"Var1 {var1}\n Var2 {var2}\n Sum {sum}\n Diff {diff}\n Prod {prod} ")

def q3():
    name = str(input("What's your name: "))
    lab = int(input("Lab note: "))
    midterm = int(input("Midterm: "))
    final = int(input("final: "))

    print(f"Last Score: {lab*25/100 + midterm*35/100 + final*40/100}")

def q4():
    print("*\n**\n***\n**\n*")
def main():
    q1()
    q2()
    q3()
    q4()



main()