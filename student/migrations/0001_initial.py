# Generated by Django 3.1.7 on 2021-02-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.BigIntegerField(unique=True)),
                ('grade', models.IntegerField()),
                ('_class', models.CharField(max_length=25)),
                ('college', models.CharField(max_length=25)),
                ('phone', models.BigIntegerField(unique=True)),
                ('base_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.wx_users')),
            ],
        ),
    ]
