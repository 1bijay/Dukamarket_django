# Generated by Django 5.0.2 on 2024-03-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/banner_imgs')),
                ('Discount_Deal', models.CharField(max_length=100)),
                ('Quote', models.CharField(max_length=150)),
                ('Discount', models.IntegerField()),
            ],
        ),
    ]