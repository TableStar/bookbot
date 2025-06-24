import sys

from stats import char_counter, dict_sorter, word_counter


def get_book_test(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    main_args = sys.argv

    if len(main_args)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    str_book = get_book_test(main_args[1])
    num = word_counter(str_book)
    char_dict = char_counter(str_book)
    list = dict_sorter(char_dict)
    print(
        "============ BOOKBOT ============\n",
        f"Analyzing book found at {main_args[1]}...\n",
        "----------- Word Count ----------\n",
        f"Found {num} total words\n",
        "--------- Character Count -------",
        sep="",
    )
    for dict in list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()
