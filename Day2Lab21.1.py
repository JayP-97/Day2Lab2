# Display a table of squares and cubes, and optionally a multiplication table
# Display a welcome message:"Learn your squares and cubes!"
# Get integer input:
# Ask the user to "Enter an integer:" Store the input as a string
# Check for valid integer:
# If the input string contains only digits...Convert the string to an integer
# If invalid input
# Print "Invalid input. Please enter an integer." Go back to the beginning of the loop
# Print table headers:
# Print "Number Squared Cubed"
# Create the table:
# For each number from 1 to the entered integer calculate its square and calculate its cube
# Print the number, its square, and its cube in a formatted table row
# If they want to continue: (y/n):"
# If the user enters "n": break out of the loop
# Print a farewell message: Good Stuff. Now you know your multiples!!


print("Powers Table")
print("Learn your squares and cubes!")

while True:
 integer_str = input("Enter an integer: ")

 if integer_str.isdigit():
   integer = int(integer_str)

   print("Number   Squared   Cubed")
   print("=======  =======  =======")

   for num in range(1, integer + 1):
     squared = num**2
     cubed = num**3
     print(f"{num:<7} {squared:<9} {cubed:<9}")

   choice = input("Want to Continue? (y/n): ").lower()
   if choice != "y":
     break

 else:
   print("Invalid input. Please enter an integer.")

print("Good Stuff. Now you know your multiples!!")