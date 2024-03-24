# Generated by Django 5.0.1 on 2024-03-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iam_app', '0004_ia_marks_batch_ia_marks_branch_ia_marks_sec_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ia_marks',
            name='ia',
            field=models.CharField(choices=[('1', 'IA 1'), ('2', 'IA 2'), ('3', 'IA 3')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='ia_marks',
            name='sec',
            field=models.CharField(max_length=2),
        ),
    ]