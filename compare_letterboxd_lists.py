import csv
import os

def extract_titles_from_csv(filepath):
    """
    Reads a CSV file, extracts titles from the 'TITLE' column, and returns them as a set.
    Handles cases where the 'TITLE' column might be missing or empty.
    """
    titles = set()
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'Title' not in reader.fieldnames:
                print(f"Warning: 'Title' column not found in {filepath}")
                return titles
            for row in reader:
                title = row.get('Title')
                if title:
                    titles.add(title.strip())
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred while reading {filepath}: {e}")
    return titles

def compare_letterboxd_lists(file1_path, file2_path, output_filename="shared_movie_titles.csv"):
    """
    Compares two Letterboxd CSV lists, finds common movie titles, and writes them to a new CSV.
    """
    print(f"Comparing titles from: {file1_path} and {file2_path}")

    titles1 = extract_titles_from_csv(file1_path)
    titles2 = extract_titles_from_csv(file2_path)

    if not titles1:
        print(f"No titles found in {file1_path}. Skipping comparison.")
        return
    if not titles2:
        print(f"No titles found in {file2_path}. Skipping comparison.")
        return

    shared_titles = sorted(list(titles1.intersection(titles2)))

    if not shared_titles:
        print("No shared movie titles found.")
        return

    # The output file should be in the same directory as the input files, or a specified directory
    # For now, let's assume it should be in the same directory as where the script is executed,
    # or handle the path more robustly. For this run, I'll place it in the base_dir.
    output_filepath = os.path.join("/home/node/.gemini/tmp/cf62d16acc353c1e5a9fd1f719820b2e1e21e41d738d1e3ec23530985226bbe2", output_filename)
    try:
        with open(output_filepath, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['SHARED_MOVIE_TITLE'])
            for title in shared_titles:
                writer.writerow([title])
        print(f"Successfully wrote {len(shared_titles)} shared titles to {output_filepath}")
    except Exception as e:
        print(f"An error occurred while writing the output file: {e}")

if __name__ == "__main__":
    # Adjust paths based on the actual location of the CSV files relative to the script execution
    base_dir = "/c/Users/gkram/my-dev-sandbox/workspace/letterboxd-compare" # Use absolute path for clarity
    file1 = os.path.join(base_dir, "Taidal Wif List - 2026-02-13T16-42_export.csv")
    file2 = os.path.join(base_dir, "Solidarity Cinema List - films in drive as of 3_3_25.csv")

    compare_letterboxd_lists(file1, file2)
