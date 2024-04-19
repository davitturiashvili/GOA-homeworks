print("1. km - miles")
print("2. miles - km")

choice = int(input('Please enter operation number (1 or 2): '))
number = float(input("Please enter number to convert it: "))

if choice == 1:
    print(number / 1.609344)
elif choice == 2:
    print(number * 1.609344)
else:
    print("Wrong choice")

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

result = (num1 + num2 + num3)