#Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# Example usage:
haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))  # Output: 2
