# Age Calculator Program

# Ask for user's name
name = input("What is your name? ")

# Ask for user's birth year
birth_year = input("What year were you born? ")

# Check data types
print("Type of name:", type(name))        # should be str
print("Type of birth_year:", type(birth_year))  # should be str

# Convert birth_year to an integer
birth_year = int(birth_year)

# Set current year
current_year = 2025

# Calculate age
age = current_year - birth_year

# Display result
print("Hello", name + "!")
print("You are", age, "years old in", current_year)
