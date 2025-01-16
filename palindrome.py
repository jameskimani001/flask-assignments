def solution(S):
    # Convert the string to a list of characters (since strings are immutable in Python)
    S = list(S)
    N = len(S)
    
    # Iterate through the string from both ends
    for i in range(N // 2):
        j = N - i - 1
        if S[i] == '?' and S[j] == '?':
            # Both are '?' so we can replace them with any letter, e.g., 'a'
            S[i] = S[j] = 'a'
        elif S[i] == '?':
            # If the left character is '?' and the right is not, match it to the right character
            S[i] = S[j]
        elif S[j] == '?':
            # If the right character is '?' and the left is not, match it to the left character
            S[j] = S[i]
        elif S[i] != S[j]:
            # If both are not '?' but they are different, it's impossible to form a palindrome
            return "NO"
    
    # Join the list back into a string and return
    return ''.join(S)


# Test the function with some test cases
print(solution("?ab??a"))  # Output: "aabbaa"
print(solution("bab??a"))  # Output: "NO"
print(solution("?a?"))     # Output: "aaa" or "zaz", etc.
