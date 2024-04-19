#3) შექმენით 2 ცვლადი სადაც შეტანილი გექნებათ ადამიანის წონა და სიმაღლე, (required_weight,required_height) რომლის მნიშვნელობაც იქნება 50 და 170 ,
# შემდეგ მომხმარებელს შემოატანინეთ მისი წონა input ფუნქციის მეშვეობითდა შეამოწმეთ მომხმარებლის წონა თუ უდრის required_weight ცვლადს და მომხარებლის სიმაღლე თუ უდრის required_height,
# აგრეთვე მეორე პრინტში შეამოწმეთ თუ აღემატება წონას და ნაკლებია სიმაღლეზე, თითქმის ყველა კომბინაცია შედარების ოპერატორების.

required_weight = 50
required_hight = 170

weight = int(input("What is your weight?:"))
hight = int(input("What is your height?:"))

print(required_weight >= weight or required_hight >= hight)
print(required_weight == weight and required_hight == hight)


# 4) მომხმარებელს შემოატანინეთ აჯიმანიებისა და ბუქნების რაოდენობა,
# ტქვენ კი შეამოწმეთ უდრის ტუ არა აჯიმანიების რაოდენობა აუცილებელს ან ბუქნების რაოდენობა აუცილებელს

required_pushups = 20
required_squarts = 10

pushups = int(input("How many pushups have you done?:"))
squarts = int(input("How many squarts have you done?:"))

print(required_pushups == pushups and required_squarts == squarts)