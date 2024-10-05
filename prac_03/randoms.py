# For question 1, the line generates random numbers between 5 and 20 inclusive. The smallest number was 11 and largest number was 19.

# Line 2 generates odd numbers between 3 and 10. The smallest number was 3 and largest was 9. No line 2 cannot produce 4.

# Line 3 generates a random floating-point number between 2.5 and 5.5. Smallest number would be 2.5 and largest would be 5.5.

import random
random_number = random.randint(1, 100)
print(random_number)
