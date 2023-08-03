from django.db import models

# Create your models here.
class Oursolutions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "راهکار ما"
        verbose_name_plural = "راهکارهای ما"

class Ourservices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خدمات ما"
        verbose_name_plural = "خدمات ما"

class Ourproducts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصولات ما"
        verbose_name_plural = "محصولات ما"