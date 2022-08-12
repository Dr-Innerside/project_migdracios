# Generated by Django 4.1 on 2022-08-12 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='상품의 이름')),
                ('desc', models.CharField(max_length=50, verbose_name='설명')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='도입일')),
                ('is_active', models.BooleanField(default=False, verbose_name='active 여부')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, verbose_name='구매일')),
                ('sub_start_date', models.DateTimeField(auto_now=True, verbose_name='구독시작일')),
                ('sub_end_date', models.DateTimeField(auto_now=True, verbose_name='구독종료일')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='구독상품')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='구독자')),
            ],
        ),
    ]
