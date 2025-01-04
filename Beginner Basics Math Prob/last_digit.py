a= int(input("Enter the base no: "))
b= int(input("Enter the pow no: "))
sum = a**b


print("Last digit is: " + str(abs(sum)%10))