"დავალება1) 0-იდან 20-ის ჩათვლით დაპრინტეთ ყველა მთელი რიცხვი."

for i in range(20 + 1):
    print(i)

"დავალება2) 50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით."
"ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი,"
"რომელსაც ციკლში მიემატება საიტერაციო ცვლადის მნიშვნელობა."
"საბოლოოდ დაპტინტეთ sum ცვლადის მნიშვნელობა"

a = 0

for i in range(50, 100 + 1):
    a = a + 1

print(a)


"დავალება3) -10-იდან 10-ის ჩათვლით დაატრიალეთ for ციკლი და იტერაცია მოახდინეთ 3-ით (გაიხსენეთ step),"
"დაპრინტეთ საიტერაციო ცვლადის მნიშვნელობა ყოველ ციკლის დატრიალებაზე"

for i in range (-10,10 + 1,3):
    print(i)