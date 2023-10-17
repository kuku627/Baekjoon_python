from itertools import combinations


def black_jack(card,N,M):

    now_diff=float('inf')
    

    for comb in combinations(card, 3):
        card_sum=sum(comb)
        if card_sum<=M and M-card_sum<now_diff:
            Best_diff=card_sum
            now_diff=M-card_sum

    return Best_diff


N,M=map(int,input().split())
card=list(map(int,input().split()))

print(black_jack(card,N,M))




