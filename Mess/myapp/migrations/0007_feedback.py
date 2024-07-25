# Generated by Django 3.2.16 on 2023-04-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20230411_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_food_quality', models.CharField(choices=[('1', '1 - Poor'), ('2', '2 - Fair'), ('3', '3 - Average'), ('4', '4 - Good'), ('5', '5 - Excellent')], default='3', max_length=2)),
                ('rating_nutrients', models.CharField(choices=[('1', '1 - Poor'), ('2', '2 - Fair'), ('3', '3 - Average'), ('4', '4 - Good'), ('5', '5 - Excellent')], default='3', max_length=2)),
                ('rating_hygiene', models.CharField(choices=[('1', '1 - Poor'), ('2', '2 - Fair'), ('3', '3 - Average'), ('4', '4 - Good'), ('5', '5 - Excellent')], default='3', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
