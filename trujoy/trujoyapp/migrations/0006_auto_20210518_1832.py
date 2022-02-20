# Generated by Django 3.2.1 on 2021-05-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trujoyapp', '0005_book_ground_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_ground',
            name='cat',
            field=models.CharField(default='Yes', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book_ground',
            name='people',
            field=models.CharField(max_length=10),
        ),
    ]
