from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Oursolutions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(blank=True, unique=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Oursolutions, self).save()

    def get_absolute_url(self):
        return reverse('html_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "راهکار ما"
        verbose_name_plural = "راهکارهای ما"

class Ourservices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Ourservices, self).save()

    def get_absolute_url(self):
        return reverse('html_page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "خدمات ما"
        verbose_name_plural = "خدمات ما"

class Ourproducts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Ourproducts, self).save()

    def get_absolute_url(self):
        return reverse('html_page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "محصولات ما"
        verbose_name_plural = "محصولات ما"


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    Category = models.ManyToManyField(Category, related_name='articles')
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
        return reverse('html_page', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"