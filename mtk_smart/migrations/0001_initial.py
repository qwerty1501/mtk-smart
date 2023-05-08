# Generated by Django 3.2.9 on 2023-03-06 11:09

from django.db import migrations, models
import mtk_smart.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Ф.И.О')),
                ('number', models.CharField(max_length=32, verbose_name='Номер телефона')),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратные связи',
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loga', models.ImageField(blank=True, null=True, upload_to=mtk_smart.services.get_upload_path, validators=[mtk_smart.services.validate_file_extension], verbose_name='Логотип нашего партнёра *(63x53)')),
                ('title_one', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description_one', models.TextField(verbose_name='Краткое описание')),
                ('title_two', models.CharField(blank=True, max_length=256, null=True, verbose_name='Подзаголовок')),
                ('description_two', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
                'db_table': 'services',
            },
        ),
    ]