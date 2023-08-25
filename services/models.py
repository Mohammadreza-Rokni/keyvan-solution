from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Oursolutions(models.Model):
    title = models.CharField(max_length=100, null=False,
                             blank=False, verbose_name='عنوان')
    description = models.TextField(
        null=False, blank=False, verbose_name='توضیحات')
    image = models.ImageField(null=False, blank=False, verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "راهکار ما"
        verbose_name_plural = "راهکارهای ما"


class Ourservices(models.Model):
    title = models.CharField(max_length=100, null=False,
                             blank=False, verbose_name='عنوان')
    description = models.TextField(
        null=False, blank=False, verbose_name='توضیحات')
    image = models.ImageField(null=False, blank=False, verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خدمات ما"
        verbose_name_plural = "خدمات ما"


class Ourproducts(models.Model):
    title = models.CharField(max_length=100, null=False,
                             blank=False, verbose_name='عنوان')
    description = models.TextField(
        null=False, blank=False, verbose_name='توضیحات')
    image = models.ImageField(null=False, blank=False, verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصولات ما"
        verbose_name_plural = "محصولات ما"


class Article(models.Model):
    title = models.CharField(null=False, blank=False,
                             max_length=100, verbose_name='عنوان')
    description = models.TextField(
        null=False, blank=False, verbose_name='توضیحات')
    reference = models.TextField(
        default=False, null=False, blank=False, verbose_name='منابع')
    image = models.ImageField(null=False, blank=False, verbose_name='عکس')
    publish = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ انتشار')
    update = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزسانی')
    slug = models.SlugField(blank=True, unique=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    class Meta:
        ordering = ('-update', '-publish')
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('services:articles_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.description[ :30]}"
