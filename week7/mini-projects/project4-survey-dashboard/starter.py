import csv
import sqlite3

# ══════════════════════════════════════════════════════════════════════════════
# STEP 1 — CREATE THE DATABASE AND TABLE
# ══════════════════════════════════════════════════════════════════════════════

conn = sqlite3.connect("survey.db")
# Using sqlite3.Row allows us to access columns by name: row["faculty"]
conn.row_factory = sqlite3.Row
db = conn.cursor()

# Create the responses table
db.execute('''CREATE TABLE IF NOT EXISTS responses (
    student_id TEXT, 
    faculty TEXT, 
    year INTEGER,
    satisfaction INTEGER, 
    favourite_tool TEXT, 
    comments TEXT
)''')

# ══════════════════════════════════════════════════════════════════════════════
# STEP 2 — READ ALL THREE CSV FILES AND INSERT ROWS
# ══════════════════════════════════════════════════════════════════════════════

csv_files = [
    "faculty_science.csv",
    "faculty_arts.csv",
    "faculty_business.csv",
]

# Clear existing data so we don't have duplicates if we run the script twice
db.execute("DELETE FROM responses")

for filename in csv_files:
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Insert each row using ? placeholders for security
                db.execute("""
                    INSERT INTO responses (student_id, faculty, year, satisfaction, favourite_tool, comments) 
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (row["student_id"], row["faculty"], int(row["year"]), 
                      int(row["satisfaction"]), row["favourite_tool"], row["comments"]))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping...")

conn.commit()
print("Database loaded successfully.\n")

# ══════════════════════════════════════════════════════════════════════════════
# STEP 3 — DASHBOARD QUERIES
# ══════════════════════════════════════════════════════════════════════════════

print("=" * 35)
print("   UNIVERSITY SURVEY DASHBOARD")
print("=" * 35)

# ── Query 1: Total responses by faculty ──────────────────────────────────────
print("\n1. Total Responses by Faculty")
rows = db.execute("SELECT faculty, COUNT(*) AS n FROM responses GROUP BY faculty ORDER BY faculty").fetchall()
total = 0
for row in rows:
    print(f"    {row['faculty']:<10}: {row['n']}")
    total += row['n']
print(f"    {'TOTAL':<10}: {total}")

# ── Query 2: Average satisfaction by year ────────────────────────────────────
print("\n2. Average Satisfaction by Year of Study")
rows = db.execute("SELECT year, ROUND(AVG(satisfaction), 1) AS avg_sat FROM responses GROUP BY year ORDER BY year").fetchall()
for row in rows:
    print(f"    Year {row['year']} : {row['avg_sat']} / 5")

# ── Query 3: Favourite tool popularity ───────────────────────────────────────
print("\n3. Favourite Tool Popularity")
rows = db.execute("SELECT favourite_tool, COUNT(*) AS n FROM responses GROUP BY favourite_tool ORDER BY n DESC").fetchall()
for row in rows:
    print(f"    {row['favourite_tool']:<10}: {row['n']:>2} votes")

# ── Query 4: Faculty comparison table ────────────────────────────────────────
print("\n4.
