# Allows us to manipulate strings
    # Helps with learning Django
    # Expressions that allows us to manipulate all types of strings

# 2 Popular uses
    # Verify strings match a particular pattern (log in verification)
    # Substitutions in a string

# Example of use. Need the module first
import re

pattern = r"eggs"
    # define the pattern. r"" lets python know we are using a regular expression that contains the string eggs
if re.match(pattern,"baconeggseggsbacon"): # this gets not found. if we use "eggseggseggsbacon" we get match found
    print('Match found')
else:
    print('No match has been found')
# Search & Find All
if re.search(pattern,"baconeggseggsbacon"): # on the otherhand, search gives us a match found
    print('Match has now been found')
else:
    print('No match has been found')

if re.findall(pattern,"baconeggseggsbacon"): # findall will find all patterns in a string.
    print('Matches have been found')
else:
    print('No match has been found')
    # OR
print(re.findall(pattern,"baconeggseggsbacon"))


# Find & Replace
string = "My name is Megan. Hi!" # Say we want to change the name
pattern = r"Megan" # We pass this into the subfunction
newstring = re.sub(pattern,"Pilahi",string) # subfunction.

print(newstring)

# Character Class
    # provide us a way to match up a specific set of characters
    # ex: how streets are named or college campus buildings.
    # a naming convention basically
    #
pattern = r"[A-Z][A-Z][0-9]" # this possition should be any letter a-z or 0-9
if re.search(pattern, "MP7"):
    print("Match has been found.")
else:
    print("No match has been found.")

# Group
    # always in ()
pattern = r"bread(eggs)*bread" #tells our code that eggs can be there 0 or more times

if re.match(pattern, "breadbread"):
    print("Matchy match!")
else:
    print("Nada")

if re.match(pattern, "breadeggseggseggsbread"):
    print("Matchy match!")
else:
    print("Nada")


# METACHARACTERS
    # Metacharacters allow us to make our regular expressions more powerful

# Dot Metacharacter
pattern = r"gr.y" # the . between gr and y means that there can be any characters in between like grey, gray, etc.

if re.match(pattern, "grpy"):
    print('A match has been found')

# Caret & Dollar metacharacter
    # Specify beginning or ending of a string
    # ^ start of a string
    # $ end of a string
    # important in learning Django
pattern = r"^gr.y$" # Unlike with search/findall, this specifies the string MUST start with g and end with y with NO repition

if re.match(pattern, "gray"):
    print('Matched!')

# Star Metacharacter
    # allows 0+ repititions of previous things (class, group, or singular character)
pattern = r"eggy(bacon)*" # this signifies that any thing right before the star can be repeated 0+ times in a string

if re.match(pattern, "eggy"): #this will be accepted along with "eggsbacon" however, not with just "bacon" because eggs is always part of the string but not bacon
    print("Matchy match!")
else:
    print("Nada")





