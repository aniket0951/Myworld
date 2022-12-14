# Generated by Django 3.2.12 on 2022-11-20 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_hospitaldepartment'),
        ('Accounts', '0003_rename_ponlineregister_onlineregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientLogin',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Product.mybasemodel')),
                ('p_name', models.CharField(blank=True, max_length=255)),
                ('doctor_name', models.CharField(max_length=255)),
                ('sick', models.CharField(blank=True, max_length=100)),
                ('appoint_date', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('Product.mybasemodel',),
        ),
    ]
