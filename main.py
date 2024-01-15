matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = 0
for row in matrix:
    min_elements = [element for element in row if element == min(row)]
    result += sum(min_elements)

 print(f"Сумма минимальных элементов из каждой строки: {result}")
