class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = str(bin(num))[2:]
        list_num = [i for i in num_bin]
        return int("".join(["0" if i == "1" else "1" for i in list_num]), 2)