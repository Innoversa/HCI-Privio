# Generated by Django 2.0.6 on 2018-08-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('language', models.TextField(max_length=50)),
                ('file_name', models.TextField(max_length=1000)),
            ],
        ),
    ]