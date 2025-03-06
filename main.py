import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <path_to_book>")
    sys.exit(1)

from stats import word_count
from stats import char_count
from stats import sort_on

def get_book_text(filepath):
    with open(filepath, "r") as f: 
        file_contents = f.read()
        return file_contents


def main():
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    w_count = word_count(content)
    c_count = char_count(content)
    sorted_chars = sort_on(c_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")

    print("============= END ===============")

    
main()