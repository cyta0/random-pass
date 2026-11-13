# Generating random passwords.

import string
import random

file0 = string.ascii_letters + string.digits + string.punctuation
file1 = list(file0)
random.shuffle(file1)

password_ = random.sample(file1, 8)
result = ''.join(password_)
print(result)

