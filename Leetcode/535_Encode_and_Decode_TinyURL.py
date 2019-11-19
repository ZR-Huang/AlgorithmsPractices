class Codec:
	def __init__(self):
		self.d = {}
		self.reverse_d = {}

	def encode(self, longUrl):
		"""Encodes a URL to a shortened URL.

		:type longUrl: str
		:rtype: str
		"""
		prefix, url = longUrl.split('//')

		if url.endswith('/'):
			url = url.rstrip('/')
			last_slash = '/'
		else:
			last_slash = ''

		url_split = url.split('/')
		for item in url_split:
			for index in range(1, len(item) + 1):
				if item[:index] in self.reverse_d:
					continue
				else:
					self.reverse_d[item[:index]] = item
					self.d[item] = item[:index]
				break

		shorUrl = '//'.join([prefix, '/'.join([self.d[item] for item in url_split])]) + last_slash
		print(shorUrl)
		return shorUrl


	def decode(self, shortUrl):
		"""Decodes a shortened URL to its original URL.

		:type shortUrl: str
		:rtype: str
		"""
		prefix, url = shortUrl.split('//')


		if url.endswith('/'):
			url = url.rstrip('/')
			last_slash = '/'
		else:
			last_slash = ''

		url_split = url.split('/')
		longUrl = '//'.join([prefix, '/'.join([self.reverse_d[item] for item in url_split])]) + last_slash
		print(longUrl)
		return longUrl


# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "http://airport.example.com/"
codec.decode(codec.encode(url))