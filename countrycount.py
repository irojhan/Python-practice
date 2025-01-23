from collections import OrderedDict

def count_votes():
    n = int(input())
    vote_count = OrderedDict()

    for _ in range(n):
        country = input().strip()
        if country in vote_count:
            vote_count[country] += 1
        else:
            vote_count[country] = 1

    sorted_votes = sorted(vote_count.items())

    for country, count in sorted_votes:
        print(country, count)

count_votes()
