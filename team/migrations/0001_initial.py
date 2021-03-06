# Generated by Django 3.1.7 on 2021-02-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('groups', models.CharField(max_length=25)),
                ('works', models.FileField(blank=True, null=True, upload_to='C:\\Users\\Administrator\\Desktop\\大学生比赛评分项目\\static\\uploads\\<django.db.models.fields.CharField>')),
                ('competition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.competition')),
                ('stu_id', models.ForeignKey(default='11111', on_delete=django.db.models.deletion.CASCADE, to='student.user_info')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.user_info')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='com_team',
            fields=[
                ('com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='organizer.competition')),
                ('Team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='com_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.CharField(max_length=5)),
                ('judge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.judger')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]
