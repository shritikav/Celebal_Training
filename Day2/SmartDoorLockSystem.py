correct_pin= int(input())
attempts=0
while attempts<3:
    pin=int(input())
    if pin==correct_pin:
        print("ACCESS GRANTED")
        break
    else:
        attempts+=1
if attempts == 3 and pin!=correct_pin:
    print("LOCKED")

