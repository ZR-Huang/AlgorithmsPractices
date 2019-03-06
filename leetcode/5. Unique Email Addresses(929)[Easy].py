test_input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def parseLocalName(self, localName):
        pos = localName.find('+')
        localName = localName[:pos] # strip string
        splits = localName.split('.')
        lastLocalName = "".join(splits)
        return lastLocalName

    def numUniqueEmails(self, emails) -> int:
        # print(emails)
        receivedEmails = set()
        for email in emails:
            localName, domainName = email.split('@')
            # print(self.parseLocalName(localName))
            localName = self.parseLocalName(localName)
            parsedEmail = localName + "@" + domainName
            receivedEmails.add(parsedEmail)
        
        return len(receivedEmails)


solver = Solution()
print(solver.numUniqueEmails(test_input))


