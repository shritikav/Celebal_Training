n= int(input())
org=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if org==rev:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
