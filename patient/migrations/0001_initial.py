# Generated by Django 2.1.5 on 2020-07-14 20:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.IntegerField()),
                ('Glucose', models.IntegerField()),
                ('BloodPressure', models.IntegerField()),
                ('SkinThickness', models.IntegerField()),
                ('Insulin', models.IntegerField()),
                ('BMI', models.IntegerField()),
                ('DiabetesPedigreeFunction', models.IntegerField()),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.DoctorInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('cp', models.IntegerField()),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField()),
                ('restecg', models.IntegerField()),
                ('thalach', models.IntegerField()),
                ('exang', models.IntegerField()),
                ('oldpeak', models.IntegerField()),
                ('slope', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.FileField(null=True, upload_to='images/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(max_length=40)),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married')], max_length=20)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WhoPredictDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('predicted_disease', models.CharField(max_length=50)),
            ],
        ),
    ]