# Generated by Django 3.2.1 on 2021-05-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trujoyapp', '0002_alter_book_ground_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_ground',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
