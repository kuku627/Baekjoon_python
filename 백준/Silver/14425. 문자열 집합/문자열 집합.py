n, m = map(int, input().split())  # n은 문자열 집합의 크기, m은 검사할 문자열의 개수
strings = set(input() for i in range(n))  # 문자열 집합을 set으로 저장
queries = [input() for i in range(m)]  # 검사할 문자열들을 리스트로 저



count=0
for query in queries:
    if query in strings:
        count+=1
print(count)