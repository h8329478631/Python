# Accept decimal num from console/terminal and convert that into binary, octal, hexadecimal num system and display back on terminal again.

input_1 = int(input("Enter the decimal num = ")) #get the input by user

print("Choose any one -\n 1. Binary\n 2. Octal\n 3. Hexadecimal")

choose = int(input("Ans - ")) #get choice by user

if choose == 1:
    Binary = bin(input_1) #convert to binary with inbuild fun
    print(f"This is the Binary num of {input_1} is",Binary)
elif choose == 2:
    Octal = oct(input_1) #convert to octal with inbuild fun
    print(f"This is the Octal num of {input_1} is",Octal)
elif choose == 3:
    Hexadecimal = hex(input_1) #convert to hexadecimal with inbuild fun
    print(f"This is the Hexadecimal num of {input_1} is",Hexadecimal)
else:
    print("Invalid number...!") # This line Execute when the user enter invalid num other than 1,2,3