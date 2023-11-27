def find_triplets(tuple_data):
    #ищем тройки, удовлетворяющие условию (средний элемент больше соседей)
    for i in range(1, len(tuple_data) - 1):
        if tuple_data[i-1] < tuple_data[i] > tuple_data[i+1]:
            #выводим элементы, предшествующие текущей тройке
            print(tuple_data[:i])

user_tuple = input("Введите элементы кортежа через пробел: ")
my_tuple = tuple(map(int, user_tuple.split()))
find_triplets(my_tuple)
