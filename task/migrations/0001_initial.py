# Generated by Django 5.0.3 on 2024-03-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('completed', models.BooleanField()),
            ],
        ),
    ]
