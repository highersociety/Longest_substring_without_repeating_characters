def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print(length_of_longest_substring("bbbbb"))       # Expected: 1
print(length_of_longest_substring("pwwkew"))      # Expected: 3
print(length_of_longest_substring(""))            # Expected: 0
print(length_of_longest_substring("abcdef"))      # Expected: 6
print(length_of_longest_substring("abcabcbb"))    # Expected: 3
print(length_of_longest_substring("dvdf"))        # Expected: 3
