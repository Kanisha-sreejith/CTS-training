def binary_search(products, key):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low + high) // 2

        if products[mid] == key:
            return mid
        elif products[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

products = [101, 105, 110, 115, 120]

key = 115

result = binary_search(products, key)

if result != -1:
    print("Product Found at Index:", result)
else:
    print("Product Not Found")