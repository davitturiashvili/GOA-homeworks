age = int(input("Please enter your age: "))

if age < 18:
    print("you are kid")
elif age >= 18 and age < 65:
    print("you are adult")
else:
    print("you are old")

for i in range(15):
    number = int(input("Please enter number: "))

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


grade = input("Please enter grade (A,B,C,D or F): ")

if grade == "A":
    print("excellent!")
elif grade == "B":
    print("Good Job!")
elif grade == "C":
    print("Yoy Passed.")
elif grade == "D":
    print("You Can Do Better.")
else:
    print("You Failed.")



num = 1

while num <10:
    print(num)
    num = num + 1
    