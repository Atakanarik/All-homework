import sqlite3

def main():
    # Connect to the database
    try:
        db = sqlite3.connect("favorites.db")
        # Use a dictionary cursor to access columns by name
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
    except sqlite3.OperationalError:
        print("Error: favorites.db not found. Run the setup script first.")
        return

    while True:
        print("\n--- SQL Explorer Menu ---")
        print("1. Show all unique languages")
        print("2. Count total votes for a specific language")
        print("3. Show top 5 most popular problems")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == "1":
            # Select unique values from the language column
            rows = cursor.execute("SELECT DISTINCT language FROM favorites ORDER BY language").fetchall()
            print("\nLanguages:")
            for row in rows:
                print(row["language"])

        elif choice == "2":
            lang = input("Enter language: ")
            # Use '?' as a placeholder to prevent SQL Injection
            row = cursor.execute("SELECT COUNT(*) AS total FROM favorites WHERE language = ?", (lang,)).fetchone()
            print(f"\nTotal votes for {lang}: {row['total']}")

        elif choice == "3":
            # Combine SQL grouping and ordering
            rows = cursor.execute("""
                SELECT problem, COUNT(*) AS count 
                FROM favorites 
                GROUP BY problem 
                ORDER BY count DESC 
                LIMIT 5
            """).fetchall()
            print("\nTop 5 Problems:")
            for row in rows:
                print(f"{row['problem']}: {row['count']} votes")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

    # Close the connection
    db.close()

if __name__ == "__main__":
    main()
