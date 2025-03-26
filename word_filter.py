from collections import Counter

def matches_pattern(word, pattern):
    if len(word) != len(pattern):
        return False
    for w_c, p_c in zip(word, pattern):
        if p_c != '_' and w_c != p_c:
            return False
    return True

def find_matching_words(letters, pattern, wordlist):
    letters = letters.lower()
    pattern = pattern.lower()
    letters_count = Counter(letters)

    result = []
    for word in wordlist:
        if not matches_pattern(word, pattern):
            continue
        word_count = Counter(word)
        if all(word_count[c] <= letters_count.get(c, 0) for c in word):
            result.append(word)
    return result
