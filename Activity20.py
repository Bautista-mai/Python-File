continu = True
count = 0

while continu == True:
    name = input("Enter a name: ").uppr().strip()

    if name == "STOP":
        print("The loop has now atopped")
        print(f"You have entered {count} number of names")
        break

    else:
        count += 1
        continue