'''Функція для розрахунку числа Фібоніччі'''
def caching_fibonacci():
    #Словник для зберігання значень, кеш
    cache: dict[int, int] = {}
    def fibonacci(n: int) -> int:
        
        #Базові випадок n<=0
        if n <= 0:
            return 0
        
        #Базовий випадок - перше число Фібоначчі
        elif n == 1:
            return 1
       
       #Повернення значення з кешу, якщо воно раніше було розраховане
        elif n in cache:
            return cache[n]
        
        #Розрахунок числа Фібоначчі рекурсивно
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        
        #Повернення збереженого значення
        return cache[n]
    
    #Повертаємо фнутрішню функцію з доступом до кеш(замикання)
    return fibonacci


def main():
    #Отримуємо функцію з власним кеш
    fib = caching_fibonacci()
    #Виводимо значення 10-го числа Фібоначчі
    print(fib(10))

if __name__ == '__main__':
    main()
    