def fibanachi(n):
    """Fibanachi sonning n hadini topish Rekursiv funksiya """
    if n in {0,1}:
        return n
    return (fibanachi(n-1)+fibanachi(n-2)) #rekursiv funksiya 
print(fibanachi(10))
# -------------------------------
def fibanacci(n):
    """Fibanchini n ta hadini chiqaruvchi funksiya+ """
    fibanacci_numbers = []
    for x in range(n):
        if x in {0,1}:
            fibanacci_numbers.append(1)
        else:
            fibanacci_numbers.append(fibanacci_numbers[x-1]+fibanacci_numbers[x-2])
    return fibanacci_numbers
print(fibanacci(6))
