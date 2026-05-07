import csv
import sys

def main():
    # Get the minimum vote count from the user
    try:
        min_votes = int(input("Minimum vote count: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(1)

    # Open the favorites.csv file for reading
    try:
        with open("favorites.csv", "r") as file:
            # Create a DictReader to access columns by their header names
            reader = csv.DictReader(file)
            
            print("\n--- Filtered Results ---")
            count_found = 0
            
            for row in reader:
                # Convert the 'votes' string from the CSV to an integer for comparison
                # Note: Adjust 'votes' and 'title' if your CSV headers are named differently
                votes = int(row["votes"])
                
                if votes >= min_votes:
                    print(f"{row['title']}: {votes}")
                    count_found += 1
            
            # Final summary
            if count_found == 0:
                print("No records found matching your criteria.")
            else:
                print(f"\nTotal matches found: {count_found}")

    except FileNotFoundError:
        print("File 'favorites.csv' not found. Make sure it's in the same folder.")

if __name__ == "__main__":
    main()
