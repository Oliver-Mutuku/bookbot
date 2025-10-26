import sys
from stats import get_book_text, get_num_words, count_characters, sort_character_counts


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    result = get_num_words(text)
    characters = count_characters(text)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(result)

    print("--------- Character Count -------")
    characters = dict(sort_character_counts(characters))
    for char, count in characters.items():
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            continue


if __name__ == "__main__":
    main()
