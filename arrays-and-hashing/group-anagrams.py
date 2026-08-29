# APPROACH:
# 

# KEY INSIGHT:
# Noticing the pattern of a unique key for each group of anagrams, this problem can 
# be solved by using a dictionary to group the strings. The key for each group can 
# be the sorted version of the string, as all anagrams will have the same sorted 
# representation.

# MISTAKE / CONFUSION:
# At first, I used a nested loop to compare each string with every other string to 
# check if they are anagrams. This approach was inefficient and led to a time 
# complexity of O(n^2 * k log k), where n is the number of strings and k is the 
# maximum length of a string. I realized that sorting each string and using it as a 
# key in a dictionary would allow me to group anagrams more efficiently.

# WHAT I LEARNED:
# As well as the solution below, I could also use defaultdict from the collections 
# module to simplify the code. This would eliminate the need to check if the key 
# exists in the dictionary before appending to the list.
#
# Combining data structures such as dictionaries and lists can lead to more efficient 
# solutions for problems involving grouping or categorization.

# COMPLEXITY:
# Time:
# Space:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in res:
                res[sorted_s] = []
            
            res[sorted_s].append(s)

        return list(res.values())