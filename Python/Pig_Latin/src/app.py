import typing


def pig_it(input_english: str) -> str:
    amount_of_sentences = input_english.split('.')
    filtered_sentences = [item for item in amount_of_sentences if item != '']
    pig_latin_words = [format_sentences(sentence) for sentence in filtered_sentences]
    return " ".join(pig_latin_words)


def format_sentences(sentences: str) -> str:
    sentence = sentences.lower()
    words = [convert_word_to_pig_latin(word) for word in sentence.split()]
    first_word = capitalise_first_letter(words[0])
    formatted = f"{first_word} {' '.join(words[1:])}." if len(words) > 1 else first_word
    return formatted


def convert_word_to_pig_latin(word) -> str:
    latin_suffix = 'ay'
    return f'{word[1:] + word[0]}{latin_suffix}'


def capitalise_first_letter(word: str) -> str:
    return f'{word[0].upper() + word[1:]}'
