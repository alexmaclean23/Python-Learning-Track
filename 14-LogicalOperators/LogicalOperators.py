# Declaration of a boolean
checkValidity = True

print()
print("####################################################")
print()

# Comparisons with and operator
checkValidity = (0 == 0 and 1 == 1)
print(checkValidity)
# True

# Comparisons with and operator
checkValidity = (0 == 0 and 1 == 0)
print(checkValidity)
# False

# Comparisons with and operator
checkValidity = (1 == 0 and 1 == 0)
print(checkValidity)
# False

print()
print("####################################################")
print()

# Comparisons with or operator
checkValidity = (0 == 0 or 1 == 1)
print(checkValidity)
# True

# Comparisons with or operator
checkValidity = (0 == 0 or 1 == 0)
print(checkValidity)
# True

# Comparisons with or operator
checkValidity = (1 == 0 or 1 == 0)
print(checkValidity)
# False

print()
print("####################################################")
print()

# Comparisons with not operator
checkValidity = not(1 == 1)
print(checkValidity)
# False

# Comparisons with not operator
checkValidity = not(1 != 1)
print(checkValidity)
# True

# Comparisons with not operator
checkValidity = not(1 > 0)
print(checkValidity)
# False

# Comparisons with not operator
checkValidity = not(1 < 0)
print(checkValidity)
# True

print()
print("####################################################")
print()