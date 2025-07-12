class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if found in substring 2 same letters
        # go back till the first occurence baasadaffs -> sadaffs
        # take that string for the next substring, get its count as well
        letters_set = set()
        counter = 0
        substring = ""
        max_counter = 0
        for c in s:
            substring += c
            if c in letters_set:
                if counter > max_counter:
                    max_counter = counter
                substring = Solution.getsuffix(substring)
                letters_set = set(substring)
                counter = len(substring)
            else:
                counter += 1
                letters_set.add(c)

        if counter > max_counter:
            max_counter = counter
        return max_counter

    def getsuffix(s: str) -> str:
        c = s[-1]
        suffix = []
        saw_c = False
        for letter in reversed(s):
            if saw_c and letter == c:
                suffix = list(reversed(suffix))
                return "".join(suffix)
            if letter == c:
                saw_c = True
            suffix.append(letter)
        suffix = list(reversed(suffix))
        return "".join(suffix)


sol = Solution()
s = "aabaab!bb"
c = sol.lengthOfLongestSubstring(s)
print(c)
