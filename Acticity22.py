def act22():
    #Function
    import os
    def activity4():
        num1 = eval(input("Enter a number : "))
        num2 = eval(input("Enter another number : "))
        answer = num1 + num2
        print("The sum of ", num1, " + ", num2,  " is ", answer,".")

    def activity6():
        x = 5
        print(x)
        x = x + 10
        print(x)
        x = x + 15
        print(x)
        x += 10
        print(x)

    def activity7():
        gold = 0
        miner = input("Hi, what is your name? ")
        isGold = input("Is the mineral gold? ")

        if isGold.lower() == "yes":
            gold = 1
            print(f"Hi {miner}, Your total number of gold is {gold}")
        else:
            print(f"Hi {miner}, Your total number of gold is {gold}")

    def activity8():
        password = input("PASSWORD : ")
        if password == "secret":
            print("Successfully Logged in")
            print("System finished")

        elif password == "hatdog":
            print("Cheesedog Logged in")
        else:
            print("Incorrect password please try again...")
            
    isContinue = True
    while isContinue:
        ask = input("Select the python file you want to open : \n1.) activity4 \n2.) activity6 \n3.) activity7 \n4.) activity8 \n5.) exit \nInput : ")
        os.system('cls')
        if ask == "1":
            print("Program is running")
            activity4()
        elif ask == "2":
            print("Program is running")
            activity6()
        elif ask == "3":
            print("Program is running")
            activity7()
        elif ask == "4":
            print("Program is running")
            activity8()
        elif ask == "5":
            break
        else:
            continue