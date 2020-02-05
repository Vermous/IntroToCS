"""
Convert a length in feet into smoots

CMS 195, Spring 2020
"""

# Read length in feet and convert it to a float type
length_in_feet = float(input('Enter a length in feet: '))

# Convert
length_in_smoots = length_in_feet / 5.5833

# Print to two decimal places
print('Length in Smoots: %.2f' % length_in_smoots)
