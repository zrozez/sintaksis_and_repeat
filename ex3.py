def func(str1, str2):
    count = 0
    if type(str1) == str and type(str2) == str:
        if len(str1)==10 and len(str2) == 10:
            for i in range(10):
                if str1[i] == str2[i]:
                    count +=1
                else:
                    continue
            count = count/10*100
        else:
            count = "Строки должны быть длиной в 10 символов"
    else:
        count = "Значения должны быть строками"
    return count

print(func('asdfghjklo', 'qseftgjuk1'))
print(func(123, 'qseftgjuk1'))
print(func('helloworld', 'bob'))
print(func('helloworld', 'helloworld'))
