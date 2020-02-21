class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum([1 if a == b else 0 for a, b in zip(guess, answer)])
        # return (guess[0] == answer[0]) + (guess[1] == answer[1]) + (guess[2] == answer[2])