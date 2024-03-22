print("1. km - miles")
print("2. miles - km")

choice = int(input('Please enter operation number (1 or 2): '))
number = float(input("Please enter number to convert it: "))

if choice == 1:
    print(number / 1.6)
elif choice == 2:
    print(number * 1.6)
else:
    print("Wrong choice")