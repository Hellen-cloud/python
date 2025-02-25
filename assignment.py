#Given a string, find the length of the longest
#substring without duplicate characters.
def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last index of each character
    char_index_map = {}
    start = 0  # Left pointer of the window
    max_length = 0  # To store the maximum length of substring

    for end in range(len(s)):  # Right pointer of the window
        # If the character is already in the window, move the start pointer
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1

        # Update the last index of the character
        char_index_map[s[end]] = end

        # Calculate the length of the current substring
        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage:
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3, because the longest substring without repeating characters is "abc"



