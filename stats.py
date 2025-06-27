def get_num_words(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        text_book = f.read()
        text_boot = text_book.strip()
        words = text_boot.split()
        return len(words)
    
def get_num_characters(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        text_book = f.read()
        text_book = text_book.strip()
        text_book = text_book.lower()
        characters = {}
        counter = 0
        for character in text_book:
            if character.isalpha():
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1
            else:
                pass
    return characters

def sorted_characters(characters_dict):
    character_count = sorted(characters_dict.items(), key=lambda item: item[1], reverse=True)
    return character_count