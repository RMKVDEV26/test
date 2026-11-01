s = str(input("enter a string: "))
s1 = s[::-1]
if s == s1:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")