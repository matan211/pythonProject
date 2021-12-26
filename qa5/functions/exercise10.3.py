def multiple_list(numbers: list):
    result = 1
    for i in numbers:
        result *= i
    return result

numbers = [7, -1, 3, 2, 8]
print(multiple_list(numbers))
