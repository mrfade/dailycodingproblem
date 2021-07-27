numbers = [1,2,3,4,5]
K = 9

def test(numbers, K):

    for i, num1 in enumerate(numbers):
        sum = 0
        nums = []

        for num2 in numbers[i:]:
            sum += num2
            nums.append(num2)

            if sum == K:
                return nums

print(test(numbers, K))
