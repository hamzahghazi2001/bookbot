from stats import word_count, char_count, sort_on


def main():
    path="books/frankenstein.txt"
    content = get_book_text(path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count(content)
    print("-------- Character Count -------")
    chr =char_count(content)
    sort_on(chr)

    

def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
        return (file_contents)

main()