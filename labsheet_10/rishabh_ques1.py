def solve(N, nums):
    count = 0

    for i in range(N):
        sum1 = 0
        temp = nums[i]

        while temp > 0:
            sum1 = sum1 + (temp % 10)
            temp = temp // 10

        for j in range(i + 1, N):
            sum2 = 0
            temp = nums[j]

            while temp > 0:
                sum2 = sum2 + (temp % 10)
                temp = temp // 10

            if sum1 == sum2:
                count = count + 1

    return count


N = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

answer = solve(N, nums)

print("Number of special pairs:", answer)