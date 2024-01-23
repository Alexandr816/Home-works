
z = None


# Вводим и выбераем
def in_t(x):

    a = input('Введите числа через пробел: ')

    if ','  in a:
        print('Без запятых')
        x = in_t(x)
    elif ' ' not in a:
        print('Через пробел')
        x = in_t(x)
    elif '.' in a:
        print('Без точек')
        x = in_t(x)
    elif ' ' in a:
        x = list(map(int, a.split()))
        global z
        z = int(input('Введите число: '))
    elif 'а' in a or 'б' in a or 'в' in a or 'г' in a or 'д' in a or 'е' in a or 'ё' in a or 'ж' in a or 'з' in a or 'и' in a or 'й' in a or 'к' in a or 'л' in a or 'м' in a or 'н' in a or 'о' in a or 'п' in a or 'р' in a or 'с' in a or 'т' in a or 'у' in a or 'ф' in a or 'х' in a or 'ц' in a or 'ч' in a or 'ш' in a or 'щ' in a or 'ъ' in a or 'ы' in a or 'ь' in a or 'э' in a or 'ю' in a or 'я':
        print('Только числа')
        x = in_t(x)

    return x






list1 = list
list1 = in_t(list1)




# Сортируем

def sor_t(a):
    d = 0
    for i in range(len(a)):
        x = a[i]
        y = i
        while y > 0 and a[y - 1] > x:
            d += 1
            a[y] = a[y - 1]
            y -= 1
        a[y] = x
    return a




list1 = sor_t(list1)




# Устанавливаем номер позиции элемента


def Looking(d,x,left,right):
    h = (left + right)//2
    if d[h] == x:
        print(f'индексы: {h-1},{h}')

    elif h == 0 and d[h] != x or h == len(d)-1 and d[h] != x:
            if len(d) > 2:
                print(f'Этого числа в последовательности нет! индкес ближайшего: {h} ')
            if len(d) == 2:
                if d[h+1] == x:
                    print(f'индексы: {h},{h +1}')
                if d[h+1] != x:
                    print(f'Этого числа в последовательности нет! индкес ближайшего: {h+1} ')


    elif d[h] > x:
        left = h-1
        if d[left] == x:
            print( f'индексы: {h-2},{h -1}')
        elif d[left] > x > d[left-1]:
            print(f'Этого числа в последовательности нет! индкес ближайших: {h-2},{h-1} ')
        else:
            Looking(d, x, 0, left)


    elif d[h] < x:
        right = h+1
        if d[right] == x:
            print(f'индексы: {h},{h +1}')
        elif right == len(d)-1 and d[h] < x:
            print(f'Этого числа в последовательности нет! индкес ближайшего: {h+1} ')
        elif d[right] < x <d[right+1]:
            print(f'Этого числа в последовательности нет! индкес ближайших: {h+1},{h+2} ')
        else:
            Looking(d,x,left=right,right=len(list1)-1)

    return '______________________________________'




print(Looking(d=list1,x=z,left=0,right=len(list1)-1))













#for i in list1:
    #print(Looking(d=list1, x=i, left=0, right=len(list1) - 1))



#1 2 3 4 5 6 7 8 9 99 666 888 1000
#1 3 5 7 9 11 13 14 15 17 19 21 23 25 27