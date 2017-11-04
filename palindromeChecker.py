def palindromeChecker(userPalindrome):
    if userPalindrome == userPalindrome[::-1]:
        print("Wahey! We have a palindrome!")
    else:
        print("Oops! That's not a palindrome...")
    return userPalindrome

userPalindrome = input("Enter your potential palindrome below: ")
palindromeChecker(userPalindrome)
