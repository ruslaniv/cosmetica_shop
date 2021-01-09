# Generated by Django 3.1.3 on 2021-01-09 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Купон'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='скидка'),
        ),
    ]
