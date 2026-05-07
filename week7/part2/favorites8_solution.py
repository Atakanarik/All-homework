import csv

# Open CSV file from the week1 relative path
with open("../week1/favorites.csv", "r") as file:

    # Use DictReader to parse each row as a dictionary
    reader = csv.DictReader(file)
    counts = {}

    # Iterate through the data to count occurrences of each language
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print results sorted by count in descending order
# The 'key=counts.get' argument tells sorted to use the values (counts) for sorting
for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
