# Generated by Django 2.1.3 on 2018-11-17 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_specialpermissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, null=True)),
                ('course', models.CharField(max_length=20, null=True)),
                ('grade_point', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]