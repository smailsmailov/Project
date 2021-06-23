from django.db import models
import time
class winter(models.Model):
    name = models.CharField("Место" , max_length=20 )
    time = models.DateTimeField("Время добавления",max_length=10)
    notes = models.TextField( "Заметки для описания " )
    notes_nature = models.TextField( "Заметки для природы " )
    notes_fun = models.TextField( "Заметки для развлечений " )
    notes_ways = models.TextField( "Заметки для маршрутов " )
    image = models.ImageField(upload_to="",verbose_name="Главная фотография")
    image1 = models.ImageField( upload_to="", verbose_name="Фото номер 1")
    image2 = models.ImageField( upload_to="", verbose_name="Фото номер 2")
    image3 = models.ImageField( upload_to="", blank=True, verbose_name="Фото номер 3" )
    image4 = models.ImageField( upload_to="", blank=True , verbose_name="Фото номер 4")
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = "Зимняя локация"
        verbose_name_plural = "Зимнии локации"


class summer(models.Model):
    name = models.CharField("Место" , max_length=20 )
    time = models.DateTimeField("Время добавления",max_length=10)
    notes = models.TextField( "Заметки для описания " )
    notes_nature = models.TextField( "Заметки для природы " )
    notes_fun = models.TextField( "Заметки для развлечений " )
    notes_ways = models.TextField( "Заметки для маршрутов " )
    image = models.ImageField(upload_to="",verbose_name="Главная фотография")
    image1 = models.ImageField( upload_to="", verbose_name="Фото номер 1")
    image2 = models.ImageField( upload_to="", verbose_name="Фото номер 2")
    image3 = models.ImageField( upload_to="", blank=True, verbose_name="Фото номер 3" )
    image4 = models.ImageField( upload_to="", blank=True , verbose_name="Фото номер 4")
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = "Летняя локация"
        verbose_name_plural = "Летнии локации"

class spring(models.Model):
    name = models.CharField("Место" , max_length=20 )
    time = models.DateTimeField("Время добавления",max_length=10)
    notes = models.TextField( "Заметки для описания " )
    notes_nature = models.TextField( "Заметки для природы " )
    notes_fun = models.TextField( "Заметки для развлечений " )
    notes_ways = models.TextField( "Заметки для маршрутов " )
    image = models.ImageField(upload_to="",verbose_name="Главная фотография")
    image1 = models.ImageField( upload_to="", verbose_name="Фото номер 1")
    image2 = models.ImageField( upload_to="", verbose_name="Фото номер 2")
    image3 = models.ImageField( upload_to="", blank=True, verbose_name="Фото номер 3" )
    image4 = models.ImageField( upload_to="", blank=True , verbose_name="Фото номер 4")
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = "Весенняя локация"
        verbose_name_plural = "Весении локации"
class autem(models.Model):
    name = models.CharField("Место" , max_length=20 )
    time = models.DateTimeField("Время добавления",max_length=10)
    notes = models.TextField("Заметки для описания ")
    notes_nature = models.TextField( "Заметки для природы " )
    notes_fun = models.TextField( "Заметки для развлечений " )
    notes_ways = models.TextField( "Заметки для маршрутов " )
    image = models.ImageField(upload_to="",verbose_name="Главная фотография",default=None)
    image1 = models.ImageField( upload_to="",verbose_name="Фото номер 1",default=None)
    image2 = models.ImageField( upload_to="" , verbose_name="Фото номер 2",default=None)
    image3 = models.ImageField( upload_to="", blank=True, verbose_name="Фото номер 3" ,default=None)
    image4 = models.ImageField( upload_to="", blank=True , verbose_name="Фото номер 4",default=None)
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = "Осенняя локация"
        verbose_name_plural = "Осении локации"

class comment(models.Model):
    name = models.TextField("Ваш никнейм")
    text = models.TextField('Комментарий')
    text_2 = models.TextField("Коментарий!",blank=True)
    text_3 = models.CharField('Время ответа',max_length=15)
    def create( self ,name , text ,text_2 ):

        self.save()
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = "Комменты"
        verbose_name_plural = 'Комент'