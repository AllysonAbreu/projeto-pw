# Generated by Django 3.2.7 on 2021-09-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepis', '0004_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]