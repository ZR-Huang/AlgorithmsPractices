'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Check every substring is a valid palindrome.
        """
        valid_palindromes = set() # store palindromes already found.
        def check(s):
            # reuse palindromes already found to speed up the checking process.
            if s[1:-1] in valid_palindromes:
                if s[0] == s[-1]:   
                    valid_palindromes.add(s)
                    return True
                else:
                    return False
            else:
                for i in range(len(s) >> 1):
                    if s[i]!=s[~i]:
                        return False
                valid_palindromes.add(s)
                return True
        
        if not s:
            return ""
        
        n = len(s)
        maximum = 0
        ans = ''
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                if check(substr) and len(substr) > maximum:
                    maximum = len(substr)
                    ans = substr

        return ans


    def longestPalindrome_v2(self, s: str) -> str:
        """
        Dynamic Programming
        dp(i,j) = true if Si...Sj is a palindrome else false
        dp(i,j) = (dp(i+1, j-1) and (Si == Sj))
        """
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return s
        
        dp = [[None] * n for _ in range(n)]
        maximum = 0
        ans_i = 0
        ans_j = 0
        # initialize 1-palindrome and 2-palindrome
        for i in range(n-1):
            dp[i][i] = True
            dp[i][i+1] = (s[i] == s[i+1])
            if dp[i][i+1]:
                    if maximum < 2:
                        maximum = 2
                        ans_i = i
                        ans_j = i+1
        dp[-1][-1] = True
    
        # start from 3-palindrome to n-palindrome
        for step in range(2, n):
            for i in range(n-step):
                # dp[i][j] = (dp[i+1][j-1] and (s[i]==s[j]))
                dp[i][i+step] = (dp[i+1][i+step-1] and s[i]==s[i+step])
                if dp[i][i+step]:
                    if maximum < step:
                        maximum = step
                        ans_i = i
                        ans_j = i + step
        
        return s[ans_i:ans_j+1]


    def longestPalindrome_v3(self, s: str) -> str:
        """
        Expand around the center, there are (2n-1) centers in totall of a string.
        """
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return s
        
        def expand(left, right):
            L, R = left, right
            while (L>=0 and R<n and s[L]==s[R]):
                L -= 1
                R += 1
            return R-L-1

        ans_i = 0
        ans_j = 0
        for i in range(n):
            length = max([expand(i,i), expand(i,i+1)])
            if length > ans_j-ans_i+1:
                ans_i = i - ((length - 1) >> 1)
                ans_j = i + (length >> 1)
        
        return s[ans_i:ans_j+1]
        

print(Solution().longestPalindrome_v3('babad'))
print(Solution().longestPalindrome_v3('cbbd'))
print(Solution().longestPalindrome_v3(''))
print(Solution().longestPalindrome_v3('a'))
print(Solution().longestPalindrome_v3("miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw"))
print(Solution().longestPalindrome_v3("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"))
                