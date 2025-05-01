def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    character_dict = {}
    low_case = text.lower()
    words = low_case.split()
    for word in words:
        for char in word:
            if char.isalpha():
                if char in character_dict:
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1
    return character_dict

def make_dict_list(text):
    sorted_words = sorted(text.items(), key=lambda pair: pair[1], reverse=True)
    new_list = [dict([item]) for item in sorted_words]
    return new_list
