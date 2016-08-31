# Defining the 'x' variable with the string "There are 10 types of people"
# The %d 'format characters' it's being used to put a decimal number into a string
x = "There are %d types of people." % 10

# Setting the variable 'binary' with a string value: binary
binary = "binary"

# Setting the variable 'do_not' with a string value: don't 
do_not = "don't"

# Setting the variable 'y' with a string value. 
# Both %s are being used to receive the output of the variables 'binary' and 'do_not'
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing the 'x' and the 'y' content. The result of line 5 and 14
print x
print y

# Setting the format characters %r to receive the output string of the variable x
# Which is defined at the line 3
print "I said: %r." % x

# In this case, the form '%s' does not make any difference. The output still is the string defined in the result of line 13
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# In this case, the string defined on 'joke_evaluation' contains the 'format character' '%r'. Even being an output of a string, it will use the %r to receive anything from the next variable.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Printing the add of strings 'w' and 'e'
print w + e
