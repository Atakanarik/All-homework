import csv

# Open CSV file from the week1 directory
with open("../week1/favorites.csv", "r") as file:

    # Create DictReader to treat each row as a dictionary
    reader = csv.DictReader(file)
    counts = {}

    # Iterate through the rows
    for row in reader:
        favorite = row["language"]
        
        # Use try-except block to handle dictionary counting
        try:
            counts[favorite] += 1
        except KeyError:
            # Initialize the key if it doesn't exist yet
            counts[favorite] = 1

# Display results
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
