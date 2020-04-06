class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # If two strings are anagrams of each other, then they both use the same letters.
        # There are two ways to check if every letter appears the same amount of times in a string:
        #     1) Sorting the string itself => O(S log S) with default sorting, O(S) with counting sort.
        #     2) Building on the idea of counting sort, and use an array of 26 values as a frequency of the letters.
        
        # Now there are also two ways to group these:
        #     1) Sort the strings by their sorted representation => O(K(N log N))
        #            K is the time used to compare two representations, which is either O(26) => O(1) or O(S) depending on which method you've used
        #     2) Use a hashmap/dictionary => O(NK)
        #            K is the time used to hash the representation, which is also O(1) or O(S) depending on which method you've used
        
        # The code below's time complexity is O(K * (N log N)), and has O(NK) space complexity.
        
        hmap = {}
        for i in strs:
            label = "".join(sorted(i))
            if label in hmap:
                hmap[label].append(i)
            else:
                hmap[label] = [i]
        return hmap.values()
