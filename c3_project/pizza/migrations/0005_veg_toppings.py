# Generated by Django 3.2.2 on 2021-05-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20210507_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veg_Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
    ]
