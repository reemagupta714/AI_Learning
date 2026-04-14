def greet():
    print("Hello, welcome to AI learning!")

greet()

def say_hello():
    print("Hello Reema")
say_hello()

def greet_user(name):
    print("Hello", name)
greet_user("Reema")
greet_user("AI Engineer")

def add_numbers(a, b):
    print(a + b)
add_numbers(5, 10)

def add(a, b):
    return a + b
result = add(10, 5)
print(result)

def multiply(a, b):
    return a * b
result = multiply(4, 6)
print(result)

def process_user(name, age):
    message = "User " + name + " is " + str(age) + " years old"
    return message

output = process_user("Reema", 25)
print(output)

def user_summary(name, city):
    message = "name: " + name + ", city: " + city
    return message

output = user_summary("Reema", "New York")
print(output)
