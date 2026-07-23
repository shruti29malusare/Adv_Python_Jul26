def count_characters(text):
    freq = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    return dict(sorted(freq.items()))


# Example
text = "Hello World 123!!"
print(count_characters(text))