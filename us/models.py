from django.db import models

# Create your models here.

FIELD_OF_ACTIVITY_CHOICES = [
    ('Product', 'Product'),
    ('Services available', 'Services available')
]

DEGREE_OF_EDUCATION_CHOICES = [ 
    ('Diploma', 'Diploma'),
    ('Associate', 'Associate'),
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('Doctorate', 'Doctorate')
]

TYPE_OF_COOPERATION_CHOICES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Project', 'Project')
]

class Contactus(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField()
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    field_of_activity = models.CharField(max_length=100, choices=FIELD_OF_ACTIVITY_CHOICES)
    activity_province = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    degree_of_education = models.CharField(max_length=100, choices=DEGREE_OF_EDUCATION_CHOICES)
    field_of_study = models.CharField(max_length=100)
    skill = models.TextField()
    history = models.IntegerField()
    type_of_cooperation = models.CharField(max_length=100, choices=TYPE_OF_COOPERATION_CHOICES)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

class Aboutus(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

class Customer(models.Model):
    logo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
  
    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"
