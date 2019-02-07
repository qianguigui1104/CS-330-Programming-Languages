
#Due: February 6th at the beginning of class

#Pam Qian

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print (s0 + "\n")

print (solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = "T"
if re.match(pattern, s0):
    print ("It starts with 'T'!" + "\n")
else:
    print ("My regex is incorrect, it should detect the 'T'!" + "\n")

print (solution_separator)


# 2) Use a regular expression to decompose the string into words and place those words intp a list.
#    Extract the first word into a variable and print it
pattern = ' '
words = re.split(pattern, s0)
print (words)
print ("\n")
first_word = words[0]
print ("The first word is: '" + first_word + "'\n")

print (solution_separator)


# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = ' '
words = re.split(pattern, s0)
for word in words:
    print (word + "\n")

print (solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
pattern_name = 'Mary'
if re.search(pattern_name, s1):
	print("Mary is in the sentence")
else:
	print("Mary is not in the sentence")

# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern_digit = '\\d{4}'
if re.search(pattern_digit, s1):
	print("The sentence contains 4 digits")
else:
	print("The sentence does not contain 4 digits")

# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
b_year = re.search(pattern_digit, s1).group()
print("This person was born in", b_year)

print (solution_separator)


# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."

# a) Write a regular expression to match the word "dog", but not the name "Dog"
pattern_dog = 'dog'

# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
output_dog = re.findall(pattern_dog, s2)

# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
output_Dog = re.findall(pattern_dog, s2, re.IGNORECASE)

# d) Write a regular expression to match "dog" or "fog"
pattern_fog = 'dog|fog'
output_fog = re.findall(pattern_fog, s2)

# e) Print all outputs.
print("Case sensitive (dog):", output_dog)
print("Case insensitive (Dog and dog):", output_Dog)
print("dog and fog:", output_fog)

print (solution_separator)


# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern_num = '\\d+'
first_num = re.search(pattern_num, s3).group()
print("First number:", first_num)

# b) Write a regular expression to extract all numbers, store them in an array, then print the array.
all_num = re.findall(pattern_num, s3)
print("\nAll numbers: ")
for num in all_num:
	print(num)

print (solution_separator)


# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern_8a = 'begin?(.+)end+'
output_8a = re.search(pattern_8a, s5).group()

# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern_8b = 'begin(.+?)end'
output_8b = re.search(pattern_8b, s5).group()

# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
pattern_8c = 'begin.+?end'
output_8c = re.findall(pattern_8c, s5)

# d) Print all outputs.
print("Outputs:")
print("8a:", output_8a)
print("8b:", output_8b)
print("8c:", output_8c)

print (solution_separator)


# 9)
s6 = "The date 5/7/1982 is trickier to get"

# a) Write a regular expression to extract the date.
pattern_date =  "([1-9]|0[1-9]|1[012])/([1-9]|0[1-9]|[12][0-9]|3[01])/(19|20)\\d\\d"

# b) Capture the date in a variable f_date
f_date = re.search(pattern_date, s6).group()

# c) Split the date and store it as month, day, year
f_date = f_date.split("/")
month = f_date[0]
day = f_date[1]
year = f_date[2]

# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
if len(month) == 1:
	month = '0'+month

if len(day) == 1:
	day = '0'+day

comp_date = year+"/"+month+"/"+day

# e) Print comp_date
print(comp_date)

print (solution_separator)

# 10) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
pattern_date =  "([1-9]|0[1-9]|1[012])/([1-9]|0[1-9]|[12][0-9]|3[01])/(\\d\\d\\d\\d)"
date_list = re.findall(pattern_date, s8)

comp_dates = []

# b) Use the code above to convert them into yyyy-mm-dd format.

for date in date_list:
	month = date[0]
	day = date[1]
	year = date[2]

	if len(month) == 1:
		month = '0'+month

	if len(day) == 1:
		day = '0'+day

	comp_date = year+"/"+month+"/"+day

	comp_dates.append(comp_date)
	
# c) Print the dates in chronological order
comp_dates.sort()
print(comp_dates)

print (solution_separator)
