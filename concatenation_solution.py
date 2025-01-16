from itertools import permutations

def solution(A):
    max_length = 0

    # Check each string in the list to see if it has duplicate characters
    def has_duplicate_chars(s):
        return len(s) != len(set(s))  # If length of string differs from its set length, it has duplicates

    # Filter out strings that have duplicate characters
    A = [s for s in A if not has_duplicate_chars(s)]
    
    # Debugging: print the list of valid strings after filtering
    print("Filtered valid strings:", A)

    # If no valid strings are left, return 0
    if not A:
        return 0

    # Check all possible permutations of the strings in A
    for perm in permutations(A):
        concat = ''.join(perm)

        # Debugging: print the concatenated result
        print(f"Checking permutation: {concat}")

        # Check if all characters are unique across the entire concatenated string
        if len(concat) == len(set(concat)):
            # If the concatenated string has all unique characters, check if it's the longest
            max_length = max(max_length, len(concat))

    return max_length

# Test cases
A1 = ["co", "dil", "ity"]  # Expected: 5
A2 = ["abc", "yyy", "def", "csv"]  # Expected: 6
A3 = ["potato", "kayak", "banana", "racecar"]  # Expected: 0
A4 = ["eva", "jqw", "tyn", "jan"]  # Expected: 9

print(solution(A1))  # Expected output: 5
print(solution(A2))  # Expected output: 6
print(solution(A3))  # Expected output: 0
print(solution(A4))  # Expected output: 9
