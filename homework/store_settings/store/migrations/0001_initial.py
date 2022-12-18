# Generated by Django 4.1.4 on 2022-12-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Наименование"
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="Количество")),
                (
                    "not_bubble_price",
                    models.IntegerField(verbose_name="Стоимость без накрутки"),
                ),
                (
                    "bubble_percentage",
                    models.IntegerField(verbose_name="Процент накрутки"),
                ),
                ("final_price", models.IntegerField(verbose_name="Итоговая стоимость")),
                ("VAT_price", models.IntegerField(verbose_name="Стоимость с НДС")),
                ("overall", models.IntegerField(verbose_name="Итоговая")),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
