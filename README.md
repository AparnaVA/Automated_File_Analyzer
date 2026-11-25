# Python Text Statistics Analyzer

## Project Description
This project is a simple Python program that analyzes text files containing customer feedback. It reads all `.txt` files from a specified folder and calculates basic text statistics.

It identifies frequently occurring words by ignoring common words (stop words) and also finds frequently occurring two-word combinations (bigrams).

All analysis results are saved as CSV reports.

## Features
- Reads all `.txt` files from a folder.
- Calculates the total number of words in each file.
- Calculates the total number of lines in each file.
- Calculates the total number of characters in each file.
- Identifies the most frequently occurring words.
- Ignores common words such as "the", "is", "and", and "a".
- Identifies frequently occurring two-word combinations (bigrams).
- Generates consolidated reports.
- Saves reports in CSV format.

## Technologies Used
- Python
- CSV module
- OS module
- Regular Expressions (`re`)
- Collections (`Counter`)

## Project Structure

```text
text_analyzer/
│
├── text_analyzer.py
├── feedback/
│   ├── feedback1.txt
│   ├── feedback2.txt
│   └── feedback3.txt
│
└── output/
    ├── text_report.csv
    ├── word_frequency.csv
    └── bigram_report.csv
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd text_analyzer
```

### 3. Add text files

Place your customer feedback `.txt` files inside the `feedback` folder.

### 4. Run the program

```bash
python text_analyzer.py
```

## Generated Reports

### 1. text_report.csv
Contains file-wise statistics:
- File name
- Total words
- Total lines
- Total characters
- Top 5 frequently occurring words

### 2. word_frequency.csv
Contains the top 20 frequently occurring meaningful words across all text files.

### 3. bigram_report.csv
Contains the top 20 frequently occurring two-word combinations across all text files.

## Example Output

### text_report.csv

| File | Words | Lines | Characters | Top Words |
|---|---:|---:|---:|---|
| feedback1.txt | 250 | 18 | 1500 | customer, service, good |
| feedback2.txt | 180 | 12 | 1050 | delivery, product, quality |
| feedback3.txt | 320 | 25 | 2100 | staff, support, excellent |

### word_frequency.csv

| Word | Frequency |
|---|---:|
| customer | 15 |
| product | 12 |
| service | 10 |

### bigram_report.csv

| Two Word Combination | Frequency |
|---|---:|
| customer service | 8 |
| product quality | 6 |
| fast delivery | 5 |
