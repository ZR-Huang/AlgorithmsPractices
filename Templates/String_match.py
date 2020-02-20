class Solution():
    def my_solution(self, A: str, B: str) -> int:
        # Brute force, time O(n*m), n=len(A), m=len(B)
        if not A:
            return -1
        i, j, n, m = 0, 0, len(A), len(B)
        while i <= n-m:
            if B[j] == A[i]:
                while j<m and B[j] == A[i+j]: j+=1
                if j == m:
                    return i
                else:
                    j = 0
            i += 1
        return -1

    def Rabin_Karp(self, A: str, B: str) -> int:
        # time O(n), n=len(A), m=len(B)
        def hash(string):
            res = 0
            for c in string:
                res += ord(c) - ord('A')
            return res
        
        def next_hash(string, hash_, index, m):
            hash_ -= (ord(string[index])-ord('A'))
            hash_ += (ord(string[index+m])-ord('A'))
            return hash_
        
        def compare(string, pattern):
            return string == pattern
        
        if not A:
            return -1
        i, n, m = 0, len(A), len(B)
        pattern_hash = hash(B)
        str_hash = hash(A[:m])
        while i <= n-m:
            if pattern_hash == str_hash and compare(A[i:i+m], B):
                return i
            if i < n-m:
                str_hash = next_hash(A, str_hash, i, m)
            i += 1
        return -1

    def Boyer_Moore(self, A: str, B: str) -> int:
        def find_bad_char(pattern, bad_char, index):
            for i in range(index-1, -1, -1):
                if pattern[i] == bad_char:
                    return i
            return -1
        
        def find_prefix(pattern, suffix):
            length = len(suffix)
            i = 0
            while i < length:
                j = 0
                while i+j < length:
                    if pattern[j] == suffix[i+j]:
                        j+=1
                    else:
                        break
                if i+j >= length:
                    return i # return the index of suffix substring
                i+=1
            return i # return the index of suffix substring
        
        if not A:
            return -1
        start, n, m = 0, len(A), len(B)
        while start <= n-m:
            # Bad character rule
            for i in range(m-1, -1, -1):
                if B[i] != A[start+i]:
                    break
            if i <= 0:
                return start
            char_index = find_bad_char(B, A[start+i], i)
            bc_offset = i-char_index if char_index >= 0 else i+1

            gs_offset = None
            if i < m-1: # if a good suffix exists
                # Good suffix rule
                char_index = find_prefix(B, B[i+1:])
                gs_offset = start+i+1+char_index

            start += max(gs_offset, bc_offset) if gs_offset else bc_offset
            
        return -1

    def kmp(self, A: str, B: str) -> int:
        def search(main_text, pattern, pmt):
            i, j = 0, 0
            while i < len(main_text) and j < len(pattern):
                if j == -1 or main_text[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    j = pmt[j]
            if j == len(pattern):
                return i - j
            else:
                return -1
        
        def getPMT(pattern):
            pmt = [0] * (len(pattern)+1)
            pmt[0] = -1
            i, j = 0, -1
            while i < len(pattern):
                if j == -1 or pattern[i] == pattern[j]:
                    i += 1
                    j += 1
                    pmt[i] = j
                else:
                    j = pmt[j]
            return pmt

        pmt = getPMT(B)
        return search(A, B, pmt)
                    
        
import time
start = time.time()
print(Solution().my_solution("abcdefgh", "cdef"))
print(Solution().my_solution("abcdefgh", "bcdg"))
print(Solution().my_solution("abcdefghijkefghijklefghijklmnopqefghijklmnopqrsturstumnopqrstulmnopqrstuvwxyz", "efghijklmnopqrstu"))
print("Brute Force:",time.time()-start)
start = time.time()
print(Solution().Rabin_Karp("abcdefgh", "cdef"))
print(Solution().Rabin_Karp("abcdefgh", "bcdg"))
print(Solution().Rabin_Karp("abcdefghijkefghijklefghijklmnopqefghijklmnopqrsturstumnopqrstulmnopqrstuvwxyz", "efghijklmnopqrstu"))
print("Rabin Karp:",time.time()-start)
start = time.time()
print(Solution().Boyer_Moore("TGGGCGAGCGGAA", "CGAGCG"))
print(Solution().Boyer_Moore("abcdefgh", "cdef"))
print(Solution().Boyer_Moore("abcdefgh", "bcdg"))
print(Solution().Boyer_Moore("abcdefghijkefghijklefghijklmnopqefghijklmnopqrsturstumnopqrstulmnopqrstuvwxyz", "efghijklmnopqrstu"))
print("Boyer Moore:",time.time()-start)
start = time.time()
print(Solution().kmp("abcdefgh", "cdef"))
print(Solution().kmp("abcdefgh", "bcdg"))
print(Solution().kmp("abcdefghijkefghijklefghijklmnopqefghijklmnopqrsturstumnopqrstulmnopqrstuvwxyz", "efghijklmnopqrstu"))
print("KMP:",time.time()-start)