def solution(a, b):
    dot_product = 0
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    return dot_product
    