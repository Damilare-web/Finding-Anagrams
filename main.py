# Check if two words are anagrams
 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if(sorted(str1) == sorted(str2)):
    print("True")
else:
    print("False")


def find_anagram(str1, str2):
    # [assignment] Add your code here

    return True

