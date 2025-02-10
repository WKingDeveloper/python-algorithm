# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = {
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        }
        s = s.lower()

        generate_s = ""

        print(f"s : {s}")
        print(f"char : {char}")
        for c in s:
            print(f"c : {c} , c in char : {c in char}")
            if c in char:
                generate_s += c

        print(f"generate_s : {generate_s}")

        if len(generate_s) < 2:
            return True

        reverse_s = generate_s[::-1]

        if reverse_s == generate_s:
            return True
        else:
            return False
