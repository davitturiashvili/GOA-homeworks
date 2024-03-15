#we have to make 10 variable book with different names and price.
#starting prices of books/veriables
Book0_first_price = 5
book1_first_price = 10
book2_first_price = 15
book2_first_price = 20
book3_first_price = 25
book4_first_price = 30
book5_fisrt_price = 35
book6_first_price = 40
book7_first_price = 45
book8_first_price = 50
book9_first_price = 55

#values of discounts

Small_discount = 10
Big_discount = 20

#declaring small discounts
book0_price_after_small_discount = Book0_first_price - (Book0_first_price * Small_discount/100)
book1_price_after_small_discount = book1_first_price - (book1_first_price * Small_discount/100)
book2_price_after_small_discount = book2_first_price - (book2_first_price * Small_discount/100)
book3_price_after_small_discount = book3_first_price - (book3_first_price * Small_discount/100)
book4_price_after_small_discount = book4_first_price - (book4_first_price * Small_discount/100)

#declaring big discounts
book5_price_after_big_discount = book5_fisrt_price - (book5_fisrt_price * Big_discount/100)
book6_price_after_big_discount = book6_first_price - (book6_first_price * Big_discount/100)
book7_price_after_big_discount = book7_first_price - (book7_first_price * Big_discount/100)
book8_price_after_big_discount = book8_first_price - (book8_first_price * Big_discount/100)
book9_price_after_big_discount = book9_first_price - (book9_first_price * Big_discount/100)

#prices of all books
#prices of small discount books:
print("The Book0 price will be" ,book0_price_after_small_discount, "Book1 price will be" ,book1_price_after_small_discount, "Book2 price will be" ,book2_price_after_small_discount,
      "Book3 price will be" ,book3_price_after_small_discount, "And Book4 price will be" ,book4_price_after_small_discount,)

#prices of big discount books:
print("The Book5 price will be" ,book5_price_after_big_discount, "Book6 price will be" ,book6_price_after_big_discount, "Book7 price will be" ,book7_price_after_big_discount,
      "Book8 price will be" ,book8_price_after_big_discount, " and Book9 price will be" ,book9_price_after_big_discount,)