from cs50 import SQL

# Connect to the SQLite database
db = SQL("sqlite:///favorites.db")

# Prompt user for a specific problem title
favorite = input("Favorite: ")

# Execute a SQL query to count occurrences of the selected problem
# The '?' placeholder prevents SQL injection attacks
rows = db.execute(
    "SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite
)

# Get the first (and only) dictionary from the list of results
row = rows[0]

# Print the value associated with the 'n' alias
print(row["n"])
