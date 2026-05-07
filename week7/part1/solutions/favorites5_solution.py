import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader to access columns by name
    reader = csv.DictReader(file)
    counts = {}

    # Iterate over file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
