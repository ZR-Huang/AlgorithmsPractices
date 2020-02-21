from collections import deque


class Solution:
	def deckRevealedIncreasing(self, deck):
		deck.sort()
		result = deque()
		while deck:
			if len(deck) == 1 or len(result) == 0:
				result.append(deck.pop())
			else:
				result.append(deck.pop())
				result.append(result.popleft())

		return list(reversed(result))


	def deckRevealedIncreasing2(self, deck):
		deck.sort()
		result = deque()
		while deck:
			if result:
				result.appendleft(result.pop())

			result.appendleft(deck.pop())

		return list(result)



print(Solution().deckRevealedIncreasing2([17,13,11,2,3,5,7]))