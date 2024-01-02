# Generated by Django 5.0 on 2024-01-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeNest', '0015_question_remove_studentlog_email_studentlog_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='spayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.BigIntegerField()),
                ('payment_id', models.CharField(max_length=200)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
