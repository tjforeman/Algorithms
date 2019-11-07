#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution




def eating_cookies(n, cache={}):

  # cookie_count = 0

  if n == 0:
    return 1

  if n <= 2:
    return n

  # if n > 2:
  #   cookie_count = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
  # return cookie_count

  if n not in cache:
    cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    
    return cache[n]

  else:
    return cache[n]

print(eating_cookies(10))
print(eating_cookies(100))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')