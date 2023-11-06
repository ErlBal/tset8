# Generated by Django 4.2.7 on 2023-11-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Ваше имя?')),
                ('phone', models.CharField(default='+996', max_length=13, verbose_name='ваш номер')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Укажите эмейл')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Укажите тег')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название контенка')),
                ('image', models.ImageField(upload_to='content/')),
                ('tags', models.ManyToManyField(to='hashtags.tag')),
            ],
        ),
    ]