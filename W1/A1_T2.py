# 1. Assign variable Name1 with string "John"
Name1 = "John"

# 2. Print variable Name1
print(Name1)

# 3. Assign variable Name2 with string "Harry"
Name2 = "Harry"

# 4. Print variable Name2
print(Name2)

# 5. Print variables Name1 and Name2 on the same row separated by a space character
# Using a comma in print() automatically adds a space between them.
print(Name1, Name2)

# 6. Print "{Name1} is eating ice cream with {Name2}".
# We use an f-string here so Python replaces the variable names with their values.
print(f"{Name1} is eating ice cream with {Name2}.")

# 7. Print "John and Harry are friends" by using the previously defined variables.
# We use an f-string again to build the sentence using the variables.
print(f"{Name1} and {Name2} are friends.")