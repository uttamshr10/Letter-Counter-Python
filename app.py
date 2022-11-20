print("Welcome to the Letter Counter App.")
name = input("\nWhat is your name: ").title().strip()
print("Hello " + name + "!")
print("I will count the number of times that a specific letter occurs in a message.")

message = input("\nPlease enter a message: ")
occur = input("Which letter would you like to count the occurrences of:")

# Standardize to lowercase
message = message.lower()
occur = occur.lower()

# Get the count and display results
occur_count = message.count(occur)
print("\n" + name + ", your message has " +
      str(occur_count) + " " + occur + "'s in it.")
