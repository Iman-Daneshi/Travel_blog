# Generated by Django 3.2.13 on 2022-06-11 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'ordering': ['-created_date']},
        ),
    ]
