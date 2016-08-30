# Getting personal information from Felipe
name = 'Felipe M. Savoia'
age = 29 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Converting "Inches" to "Centimeters"
# The basic conversion formula is 1 = 2,54
centimeters = height * 2.54

# Converting "pounds" to "kilogramas"
# The basic conversion formula is 1 = 0,453592
kilogramas = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get ir exactly right
print "\nIf I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight )

# The result of the conversion into centimeters
print "\nHis height in centimeters is: " , centimeters

# The result of the pounds into kilogramas
print "His weight in kilogramas:" , kilogramas

# Converting "kilogramas" to "pounds"
inches_final = kilogramas * 2.20462

# The result of the conversion into pounds
print "\nHis weight in pounds is approximately: %d" % inches_final
