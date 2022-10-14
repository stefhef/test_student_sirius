# print(' '.join(map(lambda x: x.capitalize(), input().replace('  ', ' ').split(
#     ' '))))  # Здесь первая буква становится заглавной, а все остальные строчными

print(' '.join(map(lambda x: x[0].upper() + x[1:] if x else '', input().split(
    ' '))))  # В данном варианте только первая буква становится заглавной, остальные без изменений
