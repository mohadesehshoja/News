# Generated by Django 5.0.3 on 2024-03-31 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsDetails', '0007_topics_mynews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='builder',
            field=models.CharField(max_length=80, verbose_name='builder'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='money',
            field=models.IntegerField(verbose_name='money'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='name',
            field=models.CharField(max_length=70, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='mynews',
            name='topic',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='NewsDetails.topics'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='topic',
            field=models.CharField(max_length=150, verbose_name='topic'),
        ),
    ]
