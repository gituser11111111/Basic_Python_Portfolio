from faker import Faker
import pandas as pd

for i in range(100):
    fake = Faker()
    print(fake.profile())


