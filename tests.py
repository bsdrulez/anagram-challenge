import NumberOfCharsToBeChangedForHalfAnagram


def run_tests():
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("abc")      == -1, "Error: test failed with odd lenght string"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("aaabbb")   ==  3, "Error: test failed for substring with all different chars"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("aAabab")   ==  2, "Error: test failed"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("ab")       ==  1, "Error: test failed for substring with all different chars"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("abcde")    == -1, "Error: test failed with odd lenght string"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("mnop")     ==  2, "Error: test failed for substring with all different chars"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("xyyx")     ==  0, "Error: test failed for substrings which are already anagrams"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("xaxbbbxx") ==  1, "Error: test failed when a carachter is repeated in the substring"
    assert NumberOfCharsToBeChangedForHalfAnagram.numberOfCharsToBeChangedForHalfAnagram("bbxxxaxb") ==  1, "Error: test failed when a carachter is repeated in the substring"

if __name__ == "__main__":
    run_tests()
    print("All tests are successful")
