import csv

# ── Step 1: Read the CSV and count languages ──────────────────────────────────
counts = {}

# Make sure the path to favorites.csv is correct relative to this file
try:
    with open("../../week1/favorites.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Get the language from the row
            language = row["language"]

            # Update counts — increment if exists, create if new
            if language in counts:
                counts[language] += 1
            else:
                counts[language] = 1
except FileNotFoundError:
    print("Error: favorites.csv not found at the specified path.")
    exit(1)

# ── Step 2: Sort by popularity (most popular first) ───────────────────────────
# sorted() returns a list of keys (languages) based on their values (counts)
sorted_languages = sorted(counts, key=counts.get, reverse=True)

# ── Step 3: Print the report ──────────────────────────────────────────────────
print("\n=== Language Popularity Report ===")

# Loop over sorted_languages with enumerate() to get rank numbers
for rank, language in enumerate(sorted_languages, start=1):
    # Retrieve the count using the language name as the key
    student_count = counts[language]
    # :<10 provides padding to keep the colon aligned
    print(f"{rank}. {language:<10} : {student_count} students")

# Print the total number of responses
total_responses = sum(counts.values())
print(f"\nTotal responses: {total_responses}")
