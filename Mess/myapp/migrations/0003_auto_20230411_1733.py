# Generated by Django 3.2.16 on 2023-04-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_feedback_feedback_feedbacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('suggestion', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='feedbacks',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Confirm',
            field=models.CharField(choices=[('Very good', 'Very good'), ('Good', 'Good'), ('Medicore', 'Medicore'), ('Bad', 'Bad'), ('Very bad', 'Very bad')], max_length=100, null=True),
        ),
    ]
