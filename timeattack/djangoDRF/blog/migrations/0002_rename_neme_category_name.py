# Generated by Django 4.0.5 on 2022-06-16 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='neme',
            new_name='name',
        ),
    ]