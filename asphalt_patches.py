def solution(S):
    N = len(S)
    patches = 0
    i = 0
    
    while i < N:
        # If there's a pothole at position i, we need to place a patch
        if S[i] == 'X':
            patches += 1
            # Skip the next 3 segments as they are covered by the patch
            i += 3
        else:
            # If no pothole, just move to the next segment
            i += 1
    
    return patches

# Test cases
print(solution(".X..X"))  # Expected: 2
print(solution("X.XXXXX.X."))  # Expected: 3
print(solution("XX.XXX.."))  # Expected: 2
print(solution("XXXX"))  # Expected: 2
