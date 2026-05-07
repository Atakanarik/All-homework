import csv
import re

def is_valid_email(email):
    # Simple regex check for '@' and '.'
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def main():
    cleaned_data = []
    errors = {
        "Missing Name": 0,
        "Invalid Email": 0,
        "Invalid Age": 0
    }

    try:
        # Step 1: Read and detect problems
        with open("messy_data.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            
            for row in reader:
                is_clean = True
                
                # Check for empty name
                if not row["name"].strip():
                    errors["Missing Name"] += 1
                    is_clean = False
                
                # Check for valid email format
                if not is_valid_email(row["email"]):
                    errors["Invalid Email"] += 1
                    is_clean = False
                
                # Check for valid age (must be a positive integer)
                try:
                    age = int(row["age"])
                    if age <= 0:
                        raise ValueError
                except ValueError:
                    errors["Invalid Age"] += 1
                    is_clean = False
                
                # If everything is fine, add to our cleaned list
                if is_clean:
                    cleaned_data.append(row)

        # Step 2: Write the cleaned version
        with open("cleaned_data.csv", "w", newline="") as output_file:
            fieldnames = ["name", "email", "age"]
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(cleaned_data)

        # Step 3: Print the Report
        print("\n--- Data Cleaning Report ---")
        for error_type, count in errors.items():
            print(f"{error_type:<15}: {count} issues found")
        
        print("-" * 30)
        print(f"Total rows processed: {len(cleaned_data) + sum(errors.values())}")
        print(f"Cleaned rows saved  : {len(cleaned_data)}")
        print("Success! Check 'cleaned_data.csv' for the results.")

    except FileNotFoundError:
        print("Error: 'messy_data.csv' not found. Please create it first.")

if __name__ == "__main__":
    main()
