# Generated by Django 2.0 on 2021-03-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_record',
            name='file_name',
            field=models.CharField(max_length=100),
        ),
    ]