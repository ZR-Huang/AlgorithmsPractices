test_input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def time(func):
    def wrapper(*args, **kw):
        import time
        start = time.time()
        for _ in range(10):
            func(*args, **kw)
        costTime = (time.time()-start)/10
        print(costTime)
        return func(*args, **kw)
    return wrapper

class Solution:
    def parseLocalName(self, localName):
        pos = localName.find('+')
        localName = localName[:pos] # strip string
        lastLocalName = "".join(localName.split('.'))
        return lastLocalName

    @time
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


class SolutionV2:
    @time
    def numUniqueEmails(self, emails) -> int:
        receivedEmails = dict()
        for email in emails:
            parsedEmail = str()
            localName, domainName = email.split('@')
            for c in localName:
                if c == '.':
                    continue
                elif c == '+':
                    break
                else:
                    parsedEmail += c
            parsedEmail += "@" + domainName
            if parsedEmail not in receivedEmails:
                receivedEmails[parsedEmail] = True
        return len(receivedEmails)


class Answer:
    @time
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

solver1 = Solution()
solver2 = SolutionV2()
solver3 = Answer()
print(solver1.numUniqueEmails(test_input))
print(solver2.numUniqueEmails(test_input))
print(solver3.numUniqueEmails(test_input))