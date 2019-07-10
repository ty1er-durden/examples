# List of Python Club 'staff' members:
staff = ["Stuart", "Craig", "Yomi"]
# Who is in the staff?
print("Staff: ", staff)
# What type of object is 'staff'?
print(" Type: ", type(staff).__name__)
# How many staff members are there?
print("Count: ", len(staff))
print("")

# We got a new staff member:
staff.append("Mahoosif Dufus")
print("Staff: ", staff)
print("")

# What else can I do to my list?
print("AVAILABLE ATTRIBUTES ON 'staff' LIST:")
for a in dir(staff):
    if not a.startswith("__"):
        print("  ", a)

# I want to remove an item from a list, but how?
print("\nGET SOME HELP ON 'remove' METHOD:\n")
print(staff.remove.__doc__)
print("")

# Mahoosif Dufus sucked so let's get rid:
staff.remove("Mahoosif Dufus")
print("Staff: ", staff)
print("")
