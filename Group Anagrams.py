class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #ASCII value approach

        res = defaultdict(list) #Storing the values and appending them as lists

        for s in strs:
            count = [0] * 26 # Create a empty array to store the character frequency of a word

            for c in s:
                count[ord(c) - ord('a')] += 1 
                #Get the ASCII value of each letter and sub it by ord('a') to get the words index in the list and for each for we increase its specific index's value by one
            
            res[tuple(count)].append(s) 
            #The key is stored as a tuple as lists cannot be stored as keys in py dict. We append the word to the tuple key. After iterations if another word creates the same tuple, then that word will be added to the tuple's value
        
        return list(res.values()) #We return the value lists wrapped in list()

        #Sorting approach

        res = defaultdict(list)

        for s in strs:

            SortedS = "".join(sorted(s)) 
            # Sort the string to get a sorted list of char. "".join joins the chars into a single word str. 

            res[SortedS].append(s)
            #The sorted word str acts as a key and upcoming words that resemble the sorted word gets appended to its value.

        return list(res.values())


