class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
    
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def word(num, idx):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + word(num % 10, 0)
            else:
                return below_20[num // 100] + " Hundred " + word(num % 100, 0)

        res = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = word(num % 1000, i) + thousands[i] + " " + res
            num //= 1000
        
        return res.strip()