# Generated by Django 5.0.2 on 2024-02-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0003_habitat_habitat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitat',
            name='habitat_image',
            field=models.ImageField(blank=True, null=True, upload_to='public/img/habitat_img/'),
        ),
    ]
