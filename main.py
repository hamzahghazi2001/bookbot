from stats import word_count, char_count, sort_on
import sys


def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path=str(sys.argv[1])
        content = get_book_text(path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        word_count(content)
        print("-------- Character Count -------")
        char_counts = char_count(content)     # dict: {'e': 44538, ...}

        char_list = []
        for ch in char_counts:               # loop over dict keys
            char_list.append({
                "name": ch,
                "num": char_counts[ch]       # pull count from dict, NOT from list
            })

        char_list.sort(reverse=True, key=sort_on)

        for item in char_list:
            print(f"{item['name']}: {item['num']}")


def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
        return (file_contents)

main()