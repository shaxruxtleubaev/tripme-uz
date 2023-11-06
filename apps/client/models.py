from django.db.models import *

class Client(Model):

    fullname = CharField(
        verbose_name='ФИО',
        max_length=128
    )

    date_of_birth = DateField(
        verbose_name='Дата рождения'
    )

    country = CharField(
        verbose_name='Страна',
        max_length=64
    )

    password_data = CharField(
        verbose_name='Данные паспорта',
        max_length=128
    )

    phone_number = CharField(
        'Номер телефона',
        max_length=32
    )

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:

        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'