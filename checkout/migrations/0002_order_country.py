# Generated by Django 3.2 on 2022-10-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=123, max_length=40),
            preserve_default=False,
        ),
    ]
