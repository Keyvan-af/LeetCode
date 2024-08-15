class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict_bills = {"5": 0, "10": 0, "20": 0}
        list_correct = []
        for bill in bills:
            dict_bills[str(bill)] = dict_bills[str(bill)] + 1
            if bill == 10:
                if dict_bills["5"] > 0:
                    dict_bills["5"] = dict_bills["5"] - 1
                    list_correct.append(1)
                else:
                    list_correct.append(0)
            if bill == 20:
                if dict_bills["5"] > 0 and dict_bills["10"] > 0:
                    dict_bills["5"] = dict_bills["5"] - 1
                    dict_bills["10"] = dict_bills["10"] - 1
                    list_correct.append(1)
                elif dict_bills["5"] > 2:
                    dict_bills["5"] = dict_bills["5"] - 3
                    list_correct.append(1)
                else:
                    list_correct.append(0)
            if bill == 5:
                    list_correct.append(1)
        if set(list_correct) == {1}:
            return True
        else:
            return False