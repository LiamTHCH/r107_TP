import unidecode
phrase=str(input("Phrase : "))
clean = ''.join(e for e in phrase if e.isalnum())
clean = clean.lower()
clean = unidecode.unidecode(clean)
print(clean)
def isPalindrome(s):
    return s == s[::-1]
print("Palindrome :",isPalindrome(clean))