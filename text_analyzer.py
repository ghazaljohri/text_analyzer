import string

def analyze_text(text):
    sentences = text.split('.')
    words = text.split()
    
    # Remove punctuation and convert to lowercase
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]
    
    # Count words, sentences, and unique words
    word_count = len(cleaned_words)
    sentence_count = len(sentences)
    unique_words = set(cleaned_words)
    
    # Find the most common word
    word_freq = {}
    for word in cleaned_words:
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    most_common_word = max(word_freq, key=word_freq.get)

    # Display results
    print("\n📊 Text Analysis Report:")
    print(f"- Total Words: {word_count}")
    print(f"- Total Sentences: {sentence_count}")
    print(f"- Unique Words: {len(unique_words)}")
    print(f"- Most Common Word: '{most_common_word}' (used {word_freq[most_common_word]} times)")

# User Input
text = input("Enter a paragraph for analysis:\n")
analyze_text(text)
