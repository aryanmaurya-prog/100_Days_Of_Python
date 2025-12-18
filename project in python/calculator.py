a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
choice = int(input("Choose Operation: "))

if choice == 1:
    print("Result:",a+b)
elif choice == 2:
    print("Result:",a-b)
elif choice == 3:
    print("Result:",a*b)
elif choice == 4:
    print("Result:",a/b)
else:
    print("Invalid Choice: ")
