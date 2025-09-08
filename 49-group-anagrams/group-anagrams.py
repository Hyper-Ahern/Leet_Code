class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Creating a 'defaultdict' subclass hashmap that handles missing keys by
        # providing a 'default'factory' callable (list) that is invoked without arguments
        final_dict = defaultdict(list)

        # For each word in the original list, sort it, join it back together, and set it as
        # a key. Then append that key into the hashmap
        for word in strs:
            key = "".join(sorted(word))
            final_dict[key].append(word)
        
        # return all the values in the hashmap as a list of lists with the original words
        # grouped in proper order to solve the problem
        return list(final_dict.values())