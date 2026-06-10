def split_into_words(all_lines):
    words = []
    for line in all_lines:
        words.extend(
            word
            for word in (word.strip(",.!?") for word in line.split())
            if word
        )
    return words
