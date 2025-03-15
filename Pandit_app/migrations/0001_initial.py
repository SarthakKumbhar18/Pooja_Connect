# Generated by Django 5.1.4 on 2025-03-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pandit',
            fields=[
                ('Pandit_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=60)),
                ('Age', models.IntegerField()),
                ('Area', models.CharField(max_length=60)),
                ('Work_Experience', models.IntegerField()),
                ('Image', models.ImageField(default='', upload_to='pandit_images/')),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
