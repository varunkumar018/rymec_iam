# Generated by Django 5.0 on 2024-02-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iam_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ia_marks',
            name='ia_1_marks',
        ),
        migrations.RemoveField(
            model_name='ia_marks',
            name='ia_2_marks',
        ),
        migrations.RemoveField(
            model_name='ia_marks',
            name='ia_3_marks',
        ),
        migrations.AddField(
            model_name='ia_marks',
            name='ia',
            field=models.CharField(choices=[('1', 'IA 1'), ('2', 'IA 2'), ('2', 'IA 3')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='ia_marks',
            name='ia_marks',
            field=models.IntegerField(default=0),
        ),
    ]