print("Program is Start")

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

try:
    if(num1 or num2 == 0):
        print("Zero divison is Not Possible")
    else:
        div = num1 / num2
        print(div)


except:
    print(div)

print("End of Program")
    
    