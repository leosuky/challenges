from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        words = file.read()
        words = words.split('\n')
        
    return words[:-1]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for i in word:
        i = i.upper()
        if i in LETTER_SCORES.keys():
            score += LETTER_SCORES[i]

    return score


def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    max_score, maxWord = 0, ''
    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score
            maxWord = word

    return maxWord

if __name__ == "__main__":
    pass # run unittests to validate
