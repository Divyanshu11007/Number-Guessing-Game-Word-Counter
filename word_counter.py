import string

REPORT_FILE = "word_frequency_report.txt"


def load_text():
    while True:
        name = input("Enter the name of the text file: ").strip()
        try:
            with open(name, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print("File not found. Please check the name and try again.")
        except PermissionError:
            print("No permission to open this file. Please try another one.")
        except OSError:
            print("This file could not be read. Please try another one.")


def get_top_n(unique_count):
    while True:
        raw = input(f"How many top words to show (1-{unique_count})? ").strip()
        try:
            n = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if n < 1 or n > unique_count:
            print(f"Enter a number between 1 and {unique_count}.")
            continue
        return n


def count_words(text):
    frequency = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if not word:
            continue
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def sorted_frequency(frequency):
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)


def ask_save_report():
    while True:
        answer = input(f"\nSave the full frequency report to {REPORT_FILE}? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def save_report(frequency, pairs, total, unique):
    lines = [
        "Word Frequency Report",
        "=" * 30,
        f"Total words: {total}",
        f"Unique words: {unique}",
        "",
    ]
    for word, count in pairs:
        lines.append(f"{word}: {count}")
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Report saved as {REPORT_FILE}.")


def main():
    print("=" * 40)
    print("   Word Counter & Frequency Analyzer")
    print("=" * 40)

    text = load_text()
    frequency = count_words(text)

    if not frequency:
        print("No words were found in this file.")
        return

    total = sum(frequency.values())
    unique = len(frequency)
    pairs = sorted_frequency(frequency)

    print(f"\nTotal words: {total}")
    print(f"Unique words: {unique}\n")

    n = get_top_n(unique)
    print(f"--- Top {n} most frequent words ---")
    for i, (word, count) in enumerate(pairs[:n], start=1):
        print(f"{i}. {word} - {count} time(s)")

    if ask_save_report():
        save_report(frequency, pairs, total, unique)


if __name__ == "__main__":
    main()
