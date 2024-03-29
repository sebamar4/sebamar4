def strip_punctuation(string):
    for c in string:
        if c in punctuation_chars: 
            string = string.replace(c, "")
    return string

def get_pos(sentence):
    positive_words_count = 0
    words_in_sentence = sentence.split(" ")
    for word in words_in_sentence:
        word = word.lower()
        word = strip_punctuation(word)
        if word in positive_words:
            positive_words_count = positive_words_count + 1
    return positive_words_count

def get_neg(sentence2):
    negative_words_count = 0
    words_in_sentence2 = sentence2.split(" ")
    for word2 in words_in_sentence2:
        word2 = word2.lower()
        word2 = strip_punctuation(word2)
        if word2 in negative_words:
            negative_words_count = negative_words_count + 1
    return negative_words_count  
