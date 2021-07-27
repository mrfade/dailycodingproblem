numbers = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]

def test(numbers):
    index = 0
    steps = 0

    while index < len(numbers) - 1:
        maxnum = 0
        maxindex = 0
        subindex = 0
        innext = numbers[index]

        for num in numbers[index+1:index+1+innext]:
            subindex += 1

            if maxnum < num:
                maxnum = num
                maxindex = subindex

        index += maxindex
        steps += 1

    return steps

print(test(numbers))
