class Solution:
    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            res+= str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        new_list = []
        i = 0

        while i < len(s):
        # i is the start of the next encoded chunk
            j = i

        # move j until it finds the #
            while s[j] != "#":
                j += 1

        # the number is between i and j
            length = int(s[i:j])

        # the word starts after # and has length characters
            word = s[j + 1 : j + 1 + length]

        # add the word to our answer
            new_list.append(word)

        # jump i to the next encoded chunk
            i = j + 1 + length

        return new_list