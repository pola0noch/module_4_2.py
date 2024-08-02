
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() # inner_function в области видимости test_function
#inner_function() # Ошибка: имя 'inner_function' не найдено




