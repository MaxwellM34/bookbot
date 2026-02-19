import sys

from stats import get_num_words, get_char_count

book = sys.argv[1]

def main():
    char_count = get_char_count(book)
    print(sys.argv)
    return char_count


if __name__ == "__main__":
    main()

