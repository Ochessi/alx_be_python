# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):  # Loop from 1 to 10
    print(f"{number} * {i} = {number * i}")
