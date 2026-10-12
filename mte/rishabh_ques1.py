def solve():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        freq = [0] * 26
        for ch in S:
            freq[ord(ch) - ord('a')] += 1
        ans = 0
        for count in freq:
            ans += count // 2
        print(ans)
solve()