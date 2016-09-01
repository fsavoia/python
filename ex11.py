print "How old are you?: ",
age = raw_input()
print "How tall are you?: ",
height = raw_input()
print "How much do you weight?: ",
weight = float(raw_input())

age = int(age)
height = float(height)

print "\n## So, you're %i old, %.2f tall and %.2f heavy." % (age, height, weight)
