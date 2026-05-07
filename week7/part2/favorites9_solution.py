from cs50 import SQL

# Connect to the SQLite database using the CS50 library
db = SQL("sqlite:///favorites.db")

# Execute a SQL query to group by language, count them, and sort by popularity
# The result is returned as a list of dictionaries
rows = db.execute(
    "SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC"
)

# Iterate through each row (dictionary) and print the language and its count
for row in rows:
    print(row["language"], row["n"])
