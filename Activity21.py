

def cute():
    print("Hello, you're cute")

def tri():
    num = int(input("Enter a number of right tringle: "))
    for i in range(1, 6):
        for y in range(1, num + 1):
            print(" ",end=" ")
            for u in range(1, i + 1):
                print("*",end=" ")
            for n in range(5,i, -1):
                print(" ",end=" ")
    print()

cute()
tri()

