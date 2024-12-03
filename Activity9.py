age = int(input("Enter your age: "))

if age > 130:
    print("Enter your real age: ")
elif age >= 60 and age <= 130:
    print("You are a senior")
elif age >= 46 and age <= 59:
    print("You are at post adulthood")
elif age >= 32 and age <= 45:
    print("You are at Mid Adulthood")
elif age >= 19 and age <= 31:
    print("You are at Early Adulthood")
elif age >= 14 and age <= 18:
    print("You are a teenager")
elif age >= 8 and age <= 1:
    print("You are at pre - teen")
elif age >= 1 and age <= 7:
    print("You are a todler")

else:
    print("Invalid input")