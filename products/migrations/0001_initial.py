# Generated by Django 4.1.1 on 2022-10-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.PositiveBigIntegerField()),
                ('specs', models.CharField(max_length=200)),
                ('band', models.CharField(max_length=200)),
            ],
        ),
    ]
