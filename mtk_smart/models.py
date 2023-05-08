from django.db import models

from .services import get_upload_path, validate_file_extension


class Services(models.Model):
    class Meta:
        db_table = 'services'
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        
    loga = models.ImageField(verbose_name="Логотип нашего партнёра *(63x53)", upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    title_one = models.CharField(verbose_name='Заголовок', max_length=256)
    description_one = models.TextField(verbose_name='Краткое описание')
    title_two = models.CharField(verbose_name='Подзаголовок', max_length=256, blank=True, null=True)
    description_two = models.TextField(verbose_name='Полное описание', blank=True, null=True)
    
    def __str__(self):
        return self.title_one
    

class Feedback(models.Model):
    
    class Meta:
        db_table = 'feedback'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        
    name = models.CharField(verbose_name="Ф.И.О", max_length=64)
    number = models.CharField(verbose_name="Номер телефона", max_length=32)
    
    def __str__(self):
        return self.name
    
        