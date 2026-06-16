import time

Range1 = int(input("Enter firs number in te range: "))
Range2 = int(input("Enter second number in te range: "))

Range2 = Range2  + 1

divisible3 = 0
divisible2 = 0
none = 0


for x in range(Range1, Range2):
    print(f"{x : 02}")
    if x %  2== 0:
        divisible2 += 1
    elif x % 3 == 0:
        divisible3 += 1
    else:
        none += 1
    time.sleep(1)


print(f"there was {divisible3 : 02}  numbers divisibles by 3 ")
print(f"there was {divisible2 : 02} numbers divisibles by 2")
print(f"there was {none} numbers divisibles  nither 2 nor 3")
