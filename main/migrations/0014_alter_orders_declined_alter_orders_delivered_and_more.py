# Generated by Django 4.1.6 on 2023-04-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='declined',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='dispatched',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_conf',
            field=models.BooleanField(default=False),
        ),
    ]
