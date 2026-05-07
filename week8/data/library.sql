import csv
import sqlite3

# 1. SETUP DATABASE
conn = sqlite3.connect("survey.db")
conn.row_factory = sqlite3.Row
db = conn.cursor()

# Create table
db.execute('''CREATE TABLE IF NOT EXISTS responses (
    student_id TEXT, faculty TEXT, year INTEGER,
    satisfaction INTEGER, favourite_tool TEXT, comments TEXT
)''')
db.execute("DELETE FROM responses") # Clear old data

# 2. LOAD DATA FROM CSVs
csv_files = ["faculty_science.csv", "faculty_arts.csv", "faculty_business.csv"]
for filename in csv_files:
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                db.execute("INSERT INTO responses VALUES (?, ?, ?, ?, ?, ?)", 
                           (row["student_id"], row["faculty"], int(row["year"]), 
                            int(row["satisfaction"]), row["favourite_tool"], row["comments"]))
    except FileNotFoundError:
        continue

conn.commit()

# 3. PRINT DASHBOARD
print("\n" + "="*35 + "\n UNIVERSITY SURVEY DASHBOARD \n" + "="*35)

# Query 1: Totals
rows = db.execute("SELECT faculty, COUNT(*) AS n FROM responses GROUP BY faculty").fetchall()
print("\n1. Responses by Faculty:")
for row in rows:
    print(f"   {row['faculty']:<10}: {row['n']}")

# Query 2: Satisfaction by Year
rows = db.execute("SELECT year, ROUND(AVG(satisfaction), 1) AS avg FROM responses GROUP BY year").fetchall()
print("\n2. Avg Satisfaction by Year:")
for row in rows:
    print(f"   Year {row['year']}: {row['avg']}/5")

# Query 3: Tool Popularity
rows = db.execute("SELECT favourite_tool, COUNT(*) AS n FROM responses GROUP BY favourite_tool ORDER BY n DESC").fetchall()
print("\n3. Tool Popularity:")
for row in rows:
    print(f"   {row['favourite_tool']:<10}: {row['n']} votes")

# Query 4: Faculty Deep Dive
print("\n4. Faculty Comparison:")
for fac in ["Arts", "Business", "Science"]:
    stats = db.execute("SELECT ROUND(AVG(satisfaction), 1) AS a FROM responses WHERE faculty = ?", (fac,)).fetchone()
    tool = db.execute("SELECT favourite_tool FROM responses WHERE faculty = ? GROUP BY favourite_tool ORDER BY COUNT(*) DESC LIMIT 1", (fac,)).fetchone()
    print(f"   {fac:<10} | Score: {stats['a'] if stats['a'] else 0} | Top Tool: {tool['favourite_tool'] if tool else 'N/A'}")

# Query 5: Interactive Filter
try:
    min_val = int(input("\nFilter - Min Satisfaction (1-5): "))
    results = db.execute("SELECT * FROM responses WHERE satisfaction >= ? ORDER BY year", (min_val,)).fetchall()
    print(f"\nResults (>= {min_val}):")
    for r in results:
        print(f"   {r['student_id']} | {r['faculty']} | Year {r['year']} | {r['favourite_tool']}")
except:
    print("Invalid input.")

conn.close()
