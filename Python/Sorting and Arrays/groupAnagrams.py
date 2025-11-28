class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}

        for st in strs:
            alphabets = [0] * 26
            for letter in st:
                alphabets[ord(letter) - ord('a')] += 1
            freq = ','.join(str(f) for f in alphabets)
            if freq not in hashmap:
                hashmap[freq] = [st]
            else:
                hashmap[freq].append(st)
        return list(hashmap.values())