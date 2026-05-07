import csv

# ── Step 1: Set up storage variables ─────────────────────────────────────────
scores = []          # we'll collect all scores here for the average
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

# We track highest and lowest as dicts so we can store the name too
highest = {"name": "", "score": -1}
lowest  = {"name": "", "score": 101}

# ── Step 2: Read the CSV ──────────────────────────────────────────────────────
# Make sure your file is named 'grades.csv' and contains the data you shared
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name  = row["name"]
        score = int(row["score"])

        # Append score to the scores list
        scores.append(score)

        # Update highest
        if score > highest["score"]:
            highest["name"] = name
            highest["score"] = score

        # Update lowest
        if score < lowest["score"]:
            lowest["name"] = name
            lowest["score"] = score

        # Determine the letter grade
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"
            
        # Increment grade_counts
        grade_counts[letter] += 1

# ── Step 3: Calculate the average ────────────────────────────────────────────
if len(scores) > 0:
    average = round(sum(scores) / len(scores), 1)
else:
    average = 0

# ── Step 4: Print the report ──────────────────────────────────────────────────
print("\n=== Quiz Grade Summary ===")
print(f"{'Average Score:':<20} {average}")
print(f"{'Highest Score:':<20} {highest['score']} ({highest['name']})")
print(f"{'Lowest Score:':<20} {lowest['score']} ({lowest['name']})")

print("\n--- Grade Distribution ---")
for grade in ["A", "B", "C", "D", "F"]:
    print(f"{grade}: {grade_counts[grade]}")

print("\nTotal students processed:", len(scores))
