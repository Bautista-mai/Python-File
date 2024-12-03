isContinue = True

while isContinue:
    name = input("Give me name: ")

    if name.lower() == "stop":
        print("Loop terminated")
        break

        isContinue = False
    else:
        print(f"Hi {name}")
        continue
