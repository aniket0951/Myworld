# Generated by Django 3.2.12 on 2022-11-06 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_hospitaldepartment'),
        ('Patient', '0005_auto_20221106_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientUpdateDetail',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Product.mybasemodel')),
                ('condition', models.CharField(max_length=255)),
                ('medicine', models.CharField(blank=True, max_length=255)),
                ('check_up', models.IntegerField()),
                ('out_patient_no', models.IntegerField()),
            ],
            bases=('Product.mybasemodel',),
        ),
        migrations.AlterField(
            model_name='pathologydep',
            name='blood_bank',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pathologydep',
            name='histopathology',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pathologydep',
            name='serology',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
