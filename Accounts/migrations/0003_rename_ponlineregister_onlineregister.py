# Generated by Django 3.2.12 on 2022-11-10 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_hospitaldepartment'),
        ('Accounts', '0002_ponlineregister'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='POnlineRegister',
            new_name='OnlineRegister',
        ),
    ]