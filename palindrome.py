#!/usr/bin/python3

#madam
#racecar
#Dammit I'm mad.
#import string
def is_palindrome(s):
    
    return s == s[::-1]

string_1 = "racecar"
string_2 = "computer"

print(is_palindrome(string_1))
print(is_palindrome(string_2))
