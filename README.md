# Letterboxd List Compare

A simple Python tool to compare two Letterboxd lists exported as CSV files and find shared movie titles between them.

## Overview

This tool takes two Letterboxd CSV export files, extracts movie titles from each list, identifies movies that appear in both lists, and outputs the shared titles to a new CSV file.

## Features

- Compare any two Letterboxd CSV exports
- Extract and normalize movie titles
- Output sorted list of shared movies to CSV
- Error handling for missing files or columns
- Simple command-line interface

## Prerequisites

- **Python 3.6+** installed on your system
- Two Letterboxd lists exported as CSV files

## How to Export Lists from Letterboxd

1. Go to [Letterboxd List Downloader](https://lizard.streamlit.app/)
2. If you prefer a local activity, check out the [lizard project](https://github.com/FastFingertips/lizard) on GitHub
3. Paste the list url or username/list-title
4. Press enter and... voilà
5. Repeat for the second list

## Installation

1. **Clone or download this repository:**
   ```bash
   git clone <your-repo-url>
   cd letterboxd-compare/compare-letterboxd-lists
   ```

2. **No additional dependencies required!** This script uses only Python standard library modules.

## Usage

### Basic Usage

1. **Edit the script** to specify your CSV file paths:
   Open `compare_letterboxd_lists.py` and modify the file paths in the `__main__` section:
   ```python
   if __name__ == "__main__":
       file1 = "/path/to/your/first-list.csv"
       file2 = "/path/to/your/second-list.csv"
       
       compare_letterboxd_lists(file1, file2)
   ```

2. **Run the script:**
   ```bash
   python compare_letterboxd_lists.py
   ```

3. **Find your output:**
   The script will create a file named `shared_movie_titles.csv` in the current directory containing all movies that appear in both lists.

### Advanced Usage (Programmatic)

You can also import and use the function in your own scripts:

```python
from compare_letterboxd_lists import compare_letterboxd_lists

# Compare two lists with custom output filename
compare_letterboxd_lists(
    file1_path="list1.csv",
    file2_path="list2.csv",
    output_filename="my_shared_movies.csv"
)
```

## Input Format

The tool expects CSV files exported from Letterboxd with the following characteristics:
- Must have a column named **"Title"** (case-sensitive)
- One movie title per row
- UTF-8 encoding recommended

Example CSV format:
```csv
Title
Surveillance
The Brick and the Mirror
Blue
```

## Output Format

The output CSV file contains:
- **Header row:** `SHARED_MOVIE_TITLE`
- **Data rows:** One shared movie title per row
- **Sorted alphabetically** for easy reading

Example output:
```csv
SHARED_MOVIE_TITLE
Blue
Surveillance
The Brick and the Mirror
```

## Error Handling

The tool handles common errors gracefully:
- **Missing files:** Prints an error message if CSV files are not found
- **Missing 'Title' column:** Warns if the expected column is not present
- **Empty lists:** Notifies if either list contains no valid titles
- **No shared movies:** Informs you when no common titles are found

## Project Structure

```
compare-letterboxd-lists/
├── compare_letterboxd_lists.py    # Main comparison script
├── shared_movie_titles.csv        # Output file (generated)
└── README.md                      # This file
```

## Deployment Options

### Option 1: Local Usage (Recommended)
Run directly on your local machine:
```bash
python compare_letterboxd_lists.py
```

### Option 2: Docker Container
Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY compare_letterboxd_lists.py .

# Mount CSV files as volumes
VOLUME ["/data"]

CMD ["python", "compare_letterboxd_lists.py"]
```

Build and run:
```bash
docker build -t letterboxd-compare .
docker run -v /path/to/your/csvs:/data letterboxd-compare
```

### Option 3: GitHub Actions Workflow
Create `.github/workflows/compare.yml`:
```yaml
name: Compare Letterboxd Lists

on:
  workflow_dispatch:
    inputs:
      list1:
        description: 'Path to first CSV'
        required: true
      list2:
        description: 'Path to second CSV'
        required: true

jobs:
  compare:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: python compare_letterboxd_lists.py
```

## Tips

- **Large lists:** The tool can handle lists with thousands of movies
- **Unicode support:** Special characters in movie titles are preserved
- **Whitespace trimming:** Leading and trailing spaces are automatically removed
- **Case sensitivity:** Titles are compared exactly as written (case-sensitive)

## Troubleshooting

### "Error: File not found"
- Check that your file paths are correct
- Use absolute paths or ensure you're running from the correct directory
- Verify the files exist before running the script

### "Warning: 'Title' column not found"
- Ensure your CSV was exported from Letterboxd properly
- Check that the column is named exactly "Title" (not "title" or "TITLE")
- Open the CSV in a text editor or spreadsheet to verify the column name

### Empty output file
- Verify both lists have movies in common
- Check that titles match exactly (spelling, punctuation, etc.)

## Support

For issues or questions, please open an issue on GitHub.
