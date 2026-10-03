# 
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and
# is decoded back to the original list of strings.

# Draft Solution:
# encode - concatenate strings with periods in between, shift 
# strings to right 3 times. The letters move from a->d, b->e etc

# decode - for each period split the string, shift each character 
# to the left 3 times.

# Thoughts on algorithm:
# Is there an easier way to do this? Seems tedious. What about long strings?
# Would looping and shifting be of great time complexity? I'm thinking O(N)
# How to shift characters: use or ord and join?

class Solution:

    def encode(self, strs: List[str]) -> str:

    def decode(self, s: str) -> List[str]:
