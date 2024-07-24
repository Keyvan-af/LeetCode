from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dicts = {mapping[i] : i for i in range(len(mapping))}
        list_T = []
        for num in nums:
            list_re = []
            for j in str(num):
                for key, value in dicts.items():
                    if int(j) == value:
                        list_re.append(key)
            list_T.append(list_re)
        numss = [''.join(map(str, sublist)) for sublist in list_T]
        m = [int(num) for num in numss]
        dict_main = {nums[i] : m[i] for i in range(len(nums))}
        sorter =  list(sorted(dict_main.items(), key=lambda x: x[1]))
        result, ress = zip(*sorter)
        return list(result)