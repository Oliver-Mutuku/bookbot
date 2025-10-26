def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text_from_book):
    num_words = text_from_book.split()
    return f"Found {len(num_words)} total words."


def count_characters(text_from_book):
    char_count = {}
    lowered_test = text_from_book.lower()

    for char in lowered_test:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_character_counts(char_counts):
    sorted_items = sorted(
        char_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_items






