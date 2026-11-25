
import os
import csv
import re
from collections import Counter

# Folder containing text files
input_folder = "feedback"

# Folder to save reports
output_folder = "output"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Common words to ignore
stop_words = {
    "the", "is", "and", "a", "an", "to", "of", "in", "on",
    "for", "with", "it", "this", "that", "was", "are", "were",
    "be", "been", "am", "as", "at", "by", "or", "but", "from",
    "i", "you", "we", "they", "he", "she", "my", "our", "your",
    "their", "me", "has", "have", "had", "do", "does", "did",
    "not", "so", "if", "can", "could", "will", "would"
}

# Store results for all files
file_reports = []

# Store all meaningful words
all_words = Counter()

# Store bigram counts
all_bigrams = Counter()

# Check whether input folder exists
if not os.path.isdir(input_folder):
    print("Input folder does not exist:", input_folder)

else:
    # Read all .txt files from the folder
    for filename in os.listdir(input_folder):

        if filename.lower().endswith(".txt"):

            file_path = os.path.join(input_folder, filename)

            # Read file contents
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            # Calculate total characters
            character_count = len(text)

            # Calculate total lines
            line_count = len(text.splitlines())

            # Extract words (letters and numbers)
            words = re.findall(r"\b[\w']+\b", text.lower())

            # Total word count
            word_count = len(words)

            # Remove common words
            meaningful_words = [
                word for word in words if word not in stop_words
            ]

            # Count meaningful words
            word_frequency = Counter(meaningful_words)

            # Add to overall word frequency
            all_words.update(meaningful_words)

            # Find top 5 frequent words in this file
            top_words = word_frequency.most_common(5)

            # Convert top words into readable text
            top_words_text = ", ".join(
                f"{word} ({count})" for word, count in top_words
            )

            # Save file statistics
            file_reports.append({
                "File": filename,
                "Words": word_count,
                "Lines": line_count,
                "Characters": character_count,
                "Top Words": top_words_text
            })

            # Find bigrams from consecutive words
            # Ignore bigrams containing stop words
            for i in range(len(words) - 1):
                first_word = words[i]
                second_word = words[i + 1]

                if first_word not in stop_words and second_word not in stop_words:
                    bigram = first_word + " " + second_word
                    all_bigrams[bigram] += 1

    # Generate file statistics CSV report
    report_path = os.path.join(output_folder, "text_report.csv")

    with open(report_path, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["File", "Words", "Lines", "Characters", "Top Words"]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(file_reports)

    # Generate overall word frequency CSV report
    word_report_path = os.path.join(output_folder, "word_frequency.csv")

    with open(word_report_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Word", "Frequency"])

        for word, count in all_words.most_common(20):
            writer.writerow([word, count])

    # Generate bigram CSV report
    bigram_report_path = os.path.join(output_folder, "bigram_report.csv")

    with open(bigram_report_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Two Word Combination", "Frequency"])

        for bigram, count in all_bigrams.most_common(20):
            writer.writerow([bigram, count])

    print("Text analysis completed successfully!")
    print("Reports saved inside the output folder.")
