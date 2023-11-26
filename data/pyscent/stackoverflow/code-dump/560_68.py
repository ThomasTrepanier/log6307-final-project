# Generated by Django 2.1.7 on 2019-03-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelOne',
            fields=[
                ('someprefix1_title', models.CharField(blank=True, default='', max_length=255)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelTwo',
            fields=[
                ('someprefix2_title', models.CharField(blank=True, default='', max_length=255)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]