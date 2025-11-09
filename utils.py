def get_book_text(path):
    with open(path, encoding='utf-8') as f: 
        return f.read()
