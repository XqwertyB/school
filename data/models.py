from django.db import models


class News(models.Model):
    name = models.CharField('Nomi', max_length=100)
    title = models.TextField('Matn')
    img = models.ImageField('Surat', upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"


class Art(models.Model):
    name = models.CharField("Nomi", max_length=100)
    img = models.ImageField("Surat", upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitoblar"
        verbose_name_plural = "Kitoblar"









