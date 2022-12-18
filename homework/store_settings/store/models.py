from django.db import models


class Product(models.Model):
    label = models.CharField('Наименование', max_length=100, unique=True)
    amount = models.IntegerField('Количество')
    not_bubble_price = models.IntegerField('Стоимость без накрутки')
    bubble_percentage = models.IntegerField('Процент накрутки')
    final_price = models.IntegerField('Итоговая стоимость')
    VAT_price = models.IntegerField('Стоимость с НДС')
    overall = models.IntegerField('Итоговая')

    def __repr__(self):
        return self.label

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
