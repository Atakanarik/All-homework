import csv

def main():
    # Dictionary to store the vote count for each language
    # Format: {language_name: vote_count}
    language_counts = {}

    try:
        # Step 1: Read the data from favorites.csv
        with open("favorites.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            
            for row in reader:
                language = row["language"]
                
                # If language is already in dict, increment; otherwise, set to 1
                if language in language_counts:
                    language_counts[language] += 1
                else:
                    language_counts[language] = 1

        # Step 2: Write the summarized data to language_summary.csv
        with open("language_summary.csv", "w", newline="") as output_file:
            # Define the headers for the new file
            fieldnames = ["language", "votes"]
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write the data rows (sorted by language name)
            for language in sorted(language_counts):
                writer.writerow({
                    "language": language,
                    "votes": language_counts[language]
                })
        
        print("Success! Results saved to 'language_summary.csv'.")

    except FileNotFoundError:
        print("Error: 'favorites.csv' not found.")

if __name__ == "__main__":
    main()
