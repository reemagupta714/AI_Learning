for i in range(5):
    print(i)

for i in range(1, 11):
    print(i)

users = ["Reema", "John", "AI"]

for user in users:
    print("Hello", user)

numbers = [10, 20, 30, 40]
for number in numbers:
    print(number * 2)

count = 1

while count <= 5:
    print(count)
    count += 1

def process_users(user_list):
    for user in user_list:
        if user == "admin":
            print(user, "→ Full access")
        else:
            print(user, "→ Limited access")

users = ["admin", "Reema", "guest"]
process_users(users)

def process_orders(order_list):
    for order in order_list:
        if order > 1000:
            print("Order", order, "→ High value")
        else:
            print("Order", order, "→ Normal value")
orders = [500, 1500, 250, 2000]
process_orders(orders)