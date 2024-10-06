class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into lists of words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Initialize two pointers for the start and the end
        i, j = 0, 0

        # Compare from the start
        while i < len(words1) and i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Compare from the end
        while j < len(words1) - i and j < len(words2) - i and words1[-(j + 1)] == words2[-(j + 1)]:
            j += 1

        # Check if the remaining part of words1 or words2 is empty or can be skipped
        return i + j >= min(len(words1), len(words2))