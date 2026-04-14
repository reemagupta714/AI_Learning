 # Day 2 - inputs, loops, conditions
name = input("Enter your name:")

city = input("Enter your city:")


print("Hello", name)
print("you live in ", city)
age = int(input("Enter your age:"))

if age >=18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")

salary = float(input("Enter your salary:"))
if salary > 1000000:
    print("High salary")
elif salary > 500000:
    print("Medium salary")
else:
    print("Low salary")



