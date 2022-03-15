def palindrome(X):
    return x == x[::-1]


x = input("Enter the word: ")
word = palindrome(x)
if word:
    print("True")
else:
    print("False")
