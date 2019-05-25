'''
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

terate over the secret string, store all the bulls in an array and keep track of the count for each character that isn't a bull in another array

Iterate over guess string, if the character isn't a bull, then remove the count of that character and increment cows
'''
import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        d = collections.defaultdict(int)
        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
            else:
                d[c] += 1
        for i, c in enumerate(guess):
            if c != secret[i] and c in d and d[c] > 0:
                cows += 1
                d[c] -= 1
        return str(bulls) + "A" + str(cows) + "B"