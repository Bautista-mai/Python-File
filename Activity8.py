prelim = int(input("Prelim Score: "))
mid = int(input("Midterm Score: "))
semi = int(input("Semi-Final Score: "))
final = int(input("Final Score: "))
quiz = int(input("Quizes Score: "))
proj = int(input('Project Score: '))

ave = (prelim * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)
print(f"Your grade is {ave}")

if ave > 100:
    print("Error. Wrong Input")
elif ave >= 65:
    print("You have passed")
else:
    print("Sorry, You failed")

