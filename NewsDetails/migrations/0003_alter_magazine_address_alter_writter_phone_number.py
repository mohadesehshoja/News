# Generated by Django 5.0.3 on 2024-03-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsDetails', '0002_alter_magazine_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='writter',
            name='phone_number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
