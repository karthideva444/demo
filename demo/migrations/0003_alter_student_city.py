# Generated by Django 5.0.3 on 2024-03-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
