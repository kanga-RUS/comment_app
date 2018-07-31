from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class City(models.Model):
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Comment(models.Model):
    last_name = models.CharField(max_length=50, blank=False, verbose_name='Фамилия')
    first_name = models.CharField(max_length=20, blank=False, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE, default='', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE, default='', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(blank=True)
    text = models.TextField(blank=False, verbose_name='Текст комментария')

    def __str__(self):
        return 'Комментарий №{}'.format(self.id)
    
    class Meta:
            ordering = ['id']
            verbose_name = 'Комметарий'
            verbose_name_plural = 'Комментарии'
