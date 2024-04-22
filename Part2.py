# Ask the user to enter the number of books they have purchased
while True:
    try:
        num_books = int(input("Enter the number of books purchased this month: "))
		# Make sure that the num_books is a positive number. Otherwise print error and ask again
        if num_books < 0:
            raise ValueError("Number of books cannot be < 0. Please enter a valid number of books.")
        break
    except ValueError as valerror:
        print(valerror)

# Calculate the points based on the number of books purchased
if num_books == 0:
    points = 0
elif num_books == 2:
    points = 5
elif num_books == 4:
    points = 15
elif num_books == 6:
    points = 30
else:
    points = 60

# Display the number of points awarded
print(f"You earned {points} award points in this month.")
