from math import comb

def count_lexicographic_vowel_strings(n):
    # Using the combinatorial formula (n + 5 - 1) choose (5 - 1)
    return comb(n + 5 - 1, 5 - 1)

# Example usage:
print(count_lexicographic_vowel_strings(1))  # Output: 5
print(count_lexicographic_vowel_strings(2))  # Output: 15
