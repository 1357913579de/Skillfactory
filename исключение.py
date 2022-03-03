# Создать
# класс
# Square.Добавить
# в
# конструктор
# класса
# Square
# собственное
# исключение
# NonPositiveDigitException, унаследованное
# от
# ValueError, которое
# будет
# срабатывать
# каждый
# раз, когда
# сторона
# квадрата
# меньше
# или
# равна
# 0.
#
# Эталон
# решения


class NonPositiveDigitException( ValueError ):
    pass


class Square:
    def __init__(self, a):
        if a < 0:
            raise NonPositiveDigitException( 'Неправильно указанна сторона квадрата' )