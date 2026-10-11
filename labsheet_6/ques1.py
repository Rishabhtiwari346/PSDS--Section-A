# Lab Sheet 6 - All Programs Combined

# QUESTION 1: 3 Sum Problem

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicate elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


print("--- QUESTION 1: 3 Sum Result ---")
nums = [1, 6, -3, 8, 1, 9, 2]
print(three_sum(nums))


# QUESTION 2: Tower of Hanoi

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, helper, source, destination)


print("\n--- QUESTION 2: Tower of Hanoi Result ---")
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')


# QUESTION 3: Fibonacci Series

print("\n--- QUESTION 3: Fibonacci Series Result ---")
n = 5
a = 1
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()