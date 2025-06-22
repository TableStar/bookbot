from stats import char_counter, word_counter


def get_book_test(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    str_book = get_book_test("books/frankenstein.txt")
    num = word_counter(str_book)
    char_dict = char_counter(str_book)
    print(f"{num} words found in the document")
    print(char_dict)


main()
