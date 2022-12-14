# Generated by Django 3.2.12 on 2022-11-06 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_hospitaldepartment'),
        ('Patient', '0004_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathologyDep',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Product.mybasemodel')),
                ('bactoriology', models.CharField(blank=True, max_length=100)),
                ('biochemistry', models.CharField(blank=True, max_length=255)),
                ('hematology', models.CharField(blank=True, max_length=255)),
                ('parasitology', models.CharField(blank=True, max_length=255)),
                ('serology', models.CharField(max_length=255)),
                ('blood_bank', models.CharField(max_length=255)),
                ('histopathology', models.CharField(blank=True, max_length=255)),
            ],
            bases=('Product.mybasemodel',),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
