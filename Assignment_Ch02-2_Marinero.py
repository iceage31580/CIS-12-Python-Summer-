# Prompt user for input
seconds = int(input("Enter the elapsed time in seconds: "))

# Calculate hours, minutes, and seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = (seconds % 3600) % 60

#print the original time
print("The elapsed time in seconds =", seconds)

# Print the converted time
print("The equivalent time in hours:minutes:seconds = {}:{}:{}".format(hours, minutes, remaining_seconds))

