import sys  
from stats import get_num_words, get_num_character
from utils import get_book_text

def print_book_report(num_words, sorted_char_counts_list, path):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    
    for char, count in sorted_char_counts_list:
        print(f"{char}: {count}")
        
    print(f"============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    file_path = sys.argv[1]
    

    try:
        book_text = get_book_text(file_path) 
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

    num_words = get_num_words(book_text)
    char_counts = get_num_character(book_text)
    
    sorted_counts_list = sorted(
        char_counts.items(), 
        key=lambda item: item[1], 
    )
    
    print_book_report(num_words, sorted_counts_list, file_path)


if __name__ == '__main__':
    main()