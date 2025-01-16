import re

def solution(S):
    # Split the text into sentences by ., ?, or !
    sentences = re.split(r'[.?!]', S)
    
    max_words = 0
    
    # Iterate through each sentence
    for sentence in sentences:
        # Split the sentence into words, removing leading/trailing spaces
        words = sentence.strip().split()
        
        # Count the valid words (those that are non-empty)
        word_count = sum(1 for word in words if word.isalpha())
        
        # Update the maximum number of words
        max_words = max(max_words, word_count)
    
    return max_words

# Test cases
print(solution("We test coders. Give us a try?"))  # Expected output: 4
print(solution("Forget CVs..Save time . x x"))     # Expected output: 2
