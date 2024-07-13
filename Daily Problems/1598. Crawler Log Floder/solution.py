class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for log in logs:
            if log == "../":
                if counter > 0:
                    counter = counter - 1
                else: 
                    counter = counter
            elif log == "./":
                counter = counter
            else:
                counter = counter + 1
        return counter