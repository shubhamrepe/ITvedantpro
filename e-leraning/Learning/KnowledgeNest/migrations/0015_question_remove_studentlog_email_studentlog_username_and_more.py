# Generated by Django 5.0 on 2023-12-28 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeNest', '0014_alter_course_name_delete_maincourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentlog',
            name='email',
        ),
        migrations.AddField(
            model_name='studentlog',
            name='username',
            field=models.CharField(default='', max_length=254, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KnowledgeNest.question')),
            ],
        ),
    ]