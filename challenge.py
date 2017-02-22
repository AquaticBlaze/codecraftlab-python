num = int(raw_input("num please"))
num1 = 1
num2 = 1
check = 0
print(num1)
if num > 0:
    while check < num-1:
        print(num2)
        num3 = num1
        num1 = num2
        num2 = num3 + num2
        check = check + 1
if num < 0:
    while check > num+1:
        print(num2)
        num3 = num1
        num1 = num2
        num2 = num3 - num2
        check = check - 1

    
    
