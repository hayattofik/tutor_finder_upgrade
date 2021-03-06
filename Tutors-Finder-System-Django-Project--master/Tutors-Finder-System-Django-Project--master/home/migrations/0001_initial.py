# Generated by Django 3.1.7 on 2021-04-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educatorType', models.CharField(max_length=20)),
                ('educatorId', models.IntegerField()),
                ('educatorName', models.CharField(max_length=30)),
                ('parentId', models.IntegerField()),
                ('parentName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educatorType', models.CharField(max_length=20)),
                ('educatorId', models.IntegerField()),
                ('educatorName', models.CharField(max_length=30)),
                ('parentId', models.IntegerField()),
                ('parentName', models.CharField(max_length=30)),
            ],
        ),
    ]
