n = int(input())
members = []

# 회원 정보 입력
for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

# 나이를 기준으로 정렬 (stable sort 사용)
sorted_members = sorted(members, key=lambda x: x[0])

# 결과 출력
for member in sorted_members:
    print(member[0], member[1])

    