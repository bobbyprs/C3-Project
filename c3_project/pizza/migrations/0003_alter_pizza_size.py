# Generated by Django 3.2.2 on 2021-05-07 08:13

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20210507_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Regular', 'REGULAR'), ('Medium', 'MEDIUM'), ('Large', 'LARGE'), ('Extra_Large', 'EXTRA_LARGE')], default=[], max_length=32),
        ),
    ]
