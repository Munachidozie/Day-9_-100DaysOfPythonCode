print ("== Generation Identifier ==")
print ("")
print ("")
print ("Ever wondered what generation you were born?")
print ("Guess what?!!! You can now!!!")

print ("Just put in your year below")
year = int(input ())

if year >= 1925 and year <= 1946:
  print ("and voila, you are a Traditionalist")
elif year >= 1947 and year <= 1964:
  print ("and voila, you are a Baby Boomer")
elif year >= 1965 and year <= 1981:
  print ("and voila, you are Generation X")
elif year >= 1982 and year <= 1995:
  print ("and voila, you are a Millenial")
elif year >= 1996 and year <= 2015:
  print ("and voila, you are Generation Z")
else:
  print ("Sorry but the year has to be between 1925 and 2015")