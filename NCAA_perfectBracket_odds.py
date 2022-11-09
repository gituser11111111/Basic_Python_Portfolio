import math
import numpy as np

odds = 2 ** 63
# odds = odds**4
# odds = odds**2

print(np.format_float_scientific(odds, precision=2, exp_digits=5))
print(odds)

'''
predicts the odds of someone filling out a perfect tournament bracket. Comes out to roughly 9.2 quintillion!
'''
