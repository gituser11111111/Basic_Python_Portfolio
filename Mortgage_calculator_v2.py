import math

Amt_Borrowed = float(input("Mortgage Amount?: "))
APR = float(input("Annual Interest Rate?: "))
N = float(input("Loan Length in Years: "))
APR = (APR / 100) / 12

N = N * 12
PMT = round(Amt_Borrowed * (math.pow(APR + 1, N) * APR) / (math.pow(1 + APR, N) - 1), 2)

print("Mortgage Amount: $", Amt_Borrowed)
print("Annual Interest Rate: %", APR)
print("Loan Length in Months: ", N)
print("Monthly Mortgage Payment: $", PMT)