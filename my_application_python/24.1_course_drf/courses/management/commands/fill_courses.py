from django.core.management import BaseCommand
from services import fill_courses


class Command(BaseCommand):
    """ Заполняет записи в таблицах по курсам (), урокам (), оплатам().
    Для курса вставляются записи в формате "Курс № <номер курса>"
    Для урока вставляются записи в формате "Урок № <номер курса>.<номер урока>"
    Для оплаты оплачиваемый курс/урок, сумма оплаты и способ оплаты подбираются случайным образом,
        в поле с датой оплаты вставляется текущая дата, в поле с кодом пользователя - код 1.
    Количество вставляемых в каждую таблицу записей подбирается случайным образом.
    Минимальное и максимальное количество записей можно настраивать в модуле fill_courses() пакета services.fill_courses

         ***Пример использования***
        > python -m manage.py fill_courses'
     """
    help = u'Заполняет базу данных с курсами случайными значениями'

    def handle(self, *args, **options):
        """Обработка вызова команды"""
        fill_courses()

