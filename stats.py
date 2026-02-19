from textwrap import dedent


def get_book_text(book):
    # utf-8-sig strips a UTF-8 BOM if present (e.g. '\ufeff' at file start).
    with open(book, encoding="utf-8-sig") as f:
        return f.read()

def get_num_words(book):
    words = get_book_text(book).split()
    return len(words)

def sort_on(items):
    return items["num"]

def get_char_count(book):
    char_count = {}
    count_list =[]
    for char in get_book_text(book):
        char = char.lower()
        if char.isalpha() == False:
            continue
        elif char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for key, num in char_count.items():
        count_list.append(dict({"char": key, "num": num}))

    count_list.sort(reverse=True, key=sort_on)
    
    text1 = dedent(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book}...
    ----------- Word Count ----------
    """).strip()
    print(text1)
    num = get_num_words(book)
    print(f"Found {num} total words")
    
    text3 = dedent("""
    --------- Character Count -------
    """).strip()
    print(text3)
    i = 0
    for pairs in count_list:
        for key, value in pairs.items():
            if i % 2 == 0:
                print(f"{value}:", end=" ")
            else:
                print(value)
            i += 1

  
    print("============= END ===============")
   
    return char_count
