class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def letter_to_position(text):
            result = []
            for char in text.lower():  # Convert text to lowercase
                if char.isalpha():  # Check if the character is a letter
                    position = ord(char) - ord('a') + 1  # Calculate the alphabet position
                    result.append(str(position))
                else:
                    result.append(char)  # Keep non-alphabet characters as they are
            return ''.join(result)

        for j in range(k):
            if j == 0:
                numbers = letter_to_position(s)
            result = 0
            for num in numbers:
                result = result + int(num)
            numbers = str(result)
        return int(numbers)