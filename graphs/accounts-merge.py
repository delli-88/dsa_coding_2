from union_find import UnionFind
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):

        emailToId = {}
        emailToName = {}
        idx = 0

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToId:
                    emailToId[email] = idx
                    idx += 1
                emailToName[email] = name

        uf = UnionFind(idx)

        for account in accounts:
            firstEmail = account[1]
            for email in account[2:]:
                uf.union(emailToId[firstEmail], emailToId[email])

        groups = defaultdict(list)
        for email in emailToId:
            parent = uf.findParent(emailToId[email])
            groups[parent].append(email)


        result = []
        for emails in groups.values():
            emails.sort()
            name = emailToName[emails[0]]
            result.append([name] + emails)

        return result

print(Solution().accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))