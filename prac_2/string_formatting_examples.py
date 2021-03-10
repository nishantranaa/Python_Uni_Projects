name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for number in numbers:
    print("Number is {:}".format(number))

# A version of the above loop using the enumerate function, useful when you want the index and value
for i, number in enumerate(numbers):
    print("Number {0} is {1:}".format(i + 1, number))

# TODO: Use string formatting to produce the output:
# the significant figures are the . to indicate the cents.
# 1922 Gibson L-5 CES for about $16,035!

print("{} {} for about ${:,.0f}!".format(year, name, cost))

# TODO: Using a for loop with the range function and string formatting,
# produce the following right-aligned output (do not use a list):
#   0
#  50
# 100
# 150

for i in range (0, 151, +10):
    print(i, end=' ')