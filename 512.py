numbers = [1, 3, 1, 2, 0, 1]
numbers2 = [1, 2, 1, 0, 0]

def test(numbers):
    index = 0
    cango = 0
    went = 0

    for number in numbers:
        if cango < number:
            cango = number
        
        if cango > 0:
            index += 1
            cango -= 1

        went += 1

    return went == index

print(test(numbers))
