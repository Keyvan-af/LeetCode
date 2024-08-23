from fractions import Fraction
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Split the expression into separate fractions
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        
        # Initialize the result as a Fraction with 0 numerator and 1 denominator
        result = Fraction(0, 1)
        
        # Add/Subtract each fraction to/from the result
        for frac in fractions:
            result += Fraction(frac)
        
        # Return the result in the form of numerator/denominator
        return f"{result.numerator}/{result.denominator}"