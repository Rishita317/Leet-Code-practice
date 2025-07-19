# this reminds me of my first intro CS class

# import requests
# import mysql.connector
# import pandas as pd

N = 7

# take user input and increment the '*" by 2 at each line below
# it looks like a christma stree"

for i in range(N):
        # Calculate the number of spaces needed before the stars
    # This centers the stars by pushing them to the right
    spaces = ' ' * (N - i - 1)
    
    # Calculate the number of stars needed for this level
    # We start with 1 star at the top, then increase by 2 on each level
    stars = '*' * (2 * i + 1)
    
    print(spaces + stars)
