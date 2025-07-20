def get_num_words(book_text):
    words = book_text.split()
    return len(words) 


def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_character_counts(char_dict):
    sorted_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list

