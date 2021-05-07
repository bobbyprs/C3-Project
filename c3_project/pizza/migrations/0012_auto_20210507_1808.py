# Generated by Django 3.2 on 2021-05-07 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0011_auto_20210507_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toopings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TypeToopings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='non_Veg_toppings',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='veg_toppings',
        ),
        migrations.DeleteModel(
            name='NonVegToopings',
        ),
        migrations.DeleteModel(
            name='VegToppings',
        ),
        migrations.AddField(
            model_name='toopings',
            name='toopings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.typetoopings'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizza.Toopings'),
        ),
    ]
