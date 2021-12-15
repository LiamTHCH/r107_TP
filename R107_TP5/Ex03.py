def estPalindrome(s):
    return s == s[::-1]

s = str(input("Entrez un mot ou une phrase : ")).lower()
if estPalindrome(s):
    print("C'est un palindrome !")
else:
    print("C'est pas un palindrome !!!!")
