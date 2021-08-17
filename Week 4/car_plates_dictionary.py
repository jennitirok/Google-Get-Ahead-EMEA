def find_shortest_word(plate, vocabulary):
    """Return the shortest word in the vocabulary with all the letters in a license plate."""

    # Filter the 'plate' string, grabing only letters in lowercase (a-z)
    word_list = []
    plate = plate.lower()
    for i in plate:
        if (ord(i) in range(97, 123)):
            word_list.append(i)

    # Iterate through the list of vocabulary and compare the letters in the plate with each vocabulary
    matching_vocabs = []
    if vocabulary == []:
        return ""

    for vocab in vocabulary:
        vocab = vocab.lower()
        matching_counter = 0
        seen = []
        for char in word_list:
            if char in vocab:
                if char in seen and vocab.count(char) == word_list.count(char):
                    matching_counter += 2
                else:
                    matching_counter += 1
                    seen.append(char)
            else:
                matching_counter = 0
                break
        matching_vocabs.append(tuple((matching_counter, vocab)))

    # Grab the highest number of matched letters
    max_counter = max([x[0] for x in matching_vocabs])

    if max_counter == 0:
        return ""

    # Filter the vocabulary, grabing only the ones with the highest max_counter
    final_list = []
    for pair in matching_vocabs:
        if (pair[0] == max_counter):
            final_list.append(pair[1])

    # Return the shortest word matched with the letters in the 'plate' string
    return min(final_list, key=len)
