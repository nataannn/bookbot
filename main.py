import sys
from stats import get_num_words, get_num_characters, sorted_characters

def get_book_text(file_path):
    file_content = ""
    with open(file_path, 'r', encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def main():

    if len (sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    total_words = get_num_words(file_path)
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    characters_dict = get_num_characters(file_path)
    ordered_characters = sorted_characters(characters_dict)

    for char, count in ordered_characters:
        print(f"{char}: {count}")

    print("============= END ===============")

main()