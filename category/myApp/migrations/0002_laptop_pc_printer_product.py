# Generated by Django 4.1.4 on 2022-12-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('model', models.IntegerField(primary_key=True, serialize=False)),
                ('speed', models.FloatField(blank=True, null=True)),
                ('ram', models.IntegerField(blank=True, null=True)),
                ('hd', models.IntegerField(blank=True, null=True)),
                ('screen', models.FloatField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'laptop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('model', models.IntegerField(primary_key=True, serialize=False)),
                ('speed', models.FloatField(blank=True, null=True)),
                ('ram', models.IntegerField(blank=True, null=True)),
                ('hd', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('model', models.IntegerField(primary_key=True, serialize=False)),
                ('color', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'printer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('maker', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
    ]
