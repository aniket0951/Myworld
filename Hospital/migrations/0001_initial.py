# Generated by Django 3.2.12 on 2022-10-28 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Product.mybasemodel')),
                ('symptoms', models.CharField(blank=True, max_length=255)),
                ('patient', models.IntegerField()),
                ('doctor_no', models.IntegerField()),
                ('appointment_date', models.DateTimeField(auto_now_add=True)),
                ('prescription_date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            bases=('Product.mybasemodel',),
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Product.mybasemodel')),
                ('name', models.CharField(max_length=255)),
                ('phone_no', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField()),
                ('blood_group', models.CharField(blank=True, max_length=100)),
                ('medicine', models.IntegerField()),
            ],
            bases=('Product.mybasemodel',),
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Product.mybasemodel')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone_no', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
            ],
            bases=('Product.mybasemodel',),
        ),
    ]
