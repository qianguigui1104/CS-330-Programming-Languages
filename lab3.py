"""Lab 3: Regexes and reformatting."""

# Pam Qian

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################

import re

new_contacts = []

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]


separator = "\n\n****************************************\n\n"
old_name = "(^[A-Z])([a-z]+)(.-?[A-Z]?(a-z)*)*((\\s)([A-Z])(\\.?|[a-z]*))?\\s[A-Z][a-z]+\\,"
old_phone = "\\(?(1-)?[0-9]{3}\\)?\\s?\\-?[0-9]+\\-?\\s?[0-9]+"
old_location = re.compile(",[A-Z][a-z]+(\\-|\\s)?[A-Z]?[a-z]*\\-?[A-Z]?[a-z]*")

for contact in contacts:

      # Find all the names
      name = re.search(old_name, contact).group()
      name = name.strip(",").split(" ")
      
      if len(name) == 2:
            first_name = name[0]
            last_name = name[1]

      else:
            first_name = name[0]
            middle_initial = name[1][0]
            last_name = name[2]

      # Print in the new format: 
      # Last name, First name, Middle Initial
      new_name = last_name + ", " + first_name + ", " + middle_initial
      

      # find all the phone numbers
      phone = re.search(old_phone, contact).group()
      phone = re.sub("\\D", "", phone) # get rid off non-didgits
      phone = re.sub("^1", "", phone) # get rid off the country code

      new_phone = "(" + phone[0] + phone[1] + phone[2]+")" + " " \
      + phone[3] + phone[4] + phone [5] + "-" \
      + phone[6] + phone[7] + phone [8] + phone [9]

      # Find all the location
      new_location = old_location.search(contact).group().strip(",")
      
      new_contacts.append([new_name, new_phone, new_location])
      

#Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
new_contacts.sort()

print("Printing by last name, ascending: \n\n")

for c in new_contacts:
      print("Name:", c[0])
      print("Tel:", c[1])
      print("Location:", c[2])
      print(separator)
