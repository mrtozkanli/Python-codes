def fibo(number):
    result=[1,1]
    for i in range(number):
        result.append(result[-1]+result[-2])
    return result

print(fibo(5))


