
number = float(input("Enter the value that you found: "))

def divide(num): #a step mentioned in the challenge hint
    return num/3

def sub(num):
    return num-3.14

def mult(num):
    return num*2*3*4*5

def addition(num):
    return num + 5

#You can see 24 different order of the given steps 
#4*3*2*1

#divide
print (divide(sub(mult(addition(number)))))

print ("\n\n")

print(divide(sub(addition(mult(number)))))

print ("\n\n")

print (divide(mult(sub(addition(number)))))

print ("\n\n")

print(divide(mult(addition(sub(number)))))

print ("\n\n")

print (divide(addition(sub(mult(number)))))

print ("\n\n")

print (divide(addition(mult(sub(number)))))

print ("\n\n")

#sum
print (addition(sub(mult(divide(number)))))

print ("\n\n")

print(addition(sub(divide(mult(number)))))

print ("\n\n")

print (addition(mult(sub(divide(number)))))

print ("\n\n")

print(addition(mult(divide(sub(number)))))

print ("\n\n")

print (addition(divide(sub(mult(number)))))

print ("\n\n")

print (addition(divide(mult(sub(number)))))

print ("\n\n")

#subtraction
print (sub(divide(mult(addition(number)))))

print ("\n\n")

print(sub(divide(addition(mult(number)))))

print ("\n\n")

print (sub(mult(divide(addition(number)))))

print ("\n\n")

print(sub(mult(addition(divide(number)))))

print ("\n\n")

print (sub(addition(divide(mult(number)))))

print ("\n\n")

print (sub(addition(mult(divide(number)))))

print ("\n\n")

#mult
print (mult(sub(div(addition(number)))))

print ("\n\n")

print(mult(sub(addition(divide(number)))))

print ("\n\n")

print (mult(divide(sub(addition(number)))))

print ("\n\n")

print(mult(divide(addition(sub(number)))))

print ("\n\n")

print (mult(divide(sub(mult(number)))))

print ("\n\n")

print (mult(addition(divide(sub(number)))))

