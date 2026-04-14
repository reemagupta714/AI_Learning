age = 20

if age > 18:
    print("You are an adult")
else:
    print("You are a minor")

marks = 75

if marks > 50:
    print("Pass")
else:
    print("Fail")

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

temperature = 30
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
elif temperature > 10:
    print("It's cool")
else:    print("It's cold") 

def check_user(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

result = check_user(20)
print(result)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def chatbot(message):
    if message == "hello":
        return "Hi there!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "I don't understand"

print(chatbot("hello"))

def user_router(role):
    if role == "admin":
        return "Full Access"
    elif role == "user":
        return "User access"
    else:
        return "Guest access"
print(user_router("admin"))