print("=== Career Agent v1 ===")

role = input("Enter your current role: ")
interest = input("What are you interested in? (AI / Cloud / Data): ").lower()
experience = int(input("Enter your years of experience: "))

# Determine path
if interest == "ai":
    path = "AI (Python, ML, LLMs)"
elif interest == "cloud":
    path = "Cloud (AWS, Terraform)"
elif interest == "data":
    path = "Data (SQL, Pandas)"
else:
    path = "Invalid choice"

# Determine level
if experience < 2:
    level = "Beginner"
elif experience <= 5:
    level = "Intermediate"
else:
    level = "Advanced"

print("You should follow", path, "path as a", level)

print("Thank you for using Career Agent")