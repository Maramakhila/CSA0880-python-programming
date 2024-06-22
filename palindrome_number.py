def palindrome(n):
    num_str=str(n)
    reversed_str=num_str[::-1]
    return num_str==reversed_str
n=int(input("enter a string:"))
if palindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not palindrome")


