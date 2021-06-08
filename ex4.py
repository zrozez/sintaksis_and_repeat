import random

def decorator_out(num):  
    def decorator_in(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_in

@decorator_out(num=7)
def func():
    num = random.randint(1, 100)
    print(f'Ваше случайное число число - {num}')


func()