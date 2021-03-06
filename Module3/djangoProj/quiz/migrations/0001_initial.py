# Generated by Django 3.0.3 on 2020-02-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_title', models.CharField(max_length=50)),
                ('answer_description', models.CharField(max_length=100)),
                ('is_correct_answer', models.BooleanField()),
                ('number_of_points', models.IntegerField()),
                ('question_foreign_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=50)),
                ('question_text', models.CharField(max_length=100)),
                ('is_multi_answer', models.BooleanField()),
                ('quiz_foreign_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=50)),
                ('quiz_description', models.CharField(max_length=100)),
                ('quiz_difficulty', models.IntegerField()),
            ],
        ),
    ]
