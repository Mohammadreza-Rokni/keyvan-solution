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


class OTP(models.Model):
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expration_code = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Contactus(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(verbose_name='تاریخ')
    full_name = models.CharField(
        max_length=200, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='شماره موبایل')
    field_of_activity = models.CharField(
        max_length=100, choices=FIELD_OF_ACTIVITY_CHOICES, verbose_name='حوضه فعالیت')
    activity_province = models.CharField(
        max_length=100, verbose_name='استان فعالیت')
    date_of_birth = models.DateField(verbose_name='تاریخ تولد')
    degree_of_education = models.CharField(
        max_length=100, choices=DEGREE_OF_EDUCATION_CHOICES, verbose_name='میزان تحصیلات')
    field_of_study = models.CharField(
        max_length=100, verbose_name='رشته تحصیلی')
    skill = models.TextField(verbose_name='مهارت')
    history = models.IntegerField(verbose_name='تجربه')
    type_of_cooperation = models.CharField(
        max_length=100, choices=TYPE_OF_COOPERATION_CHOICES, verbose_name='نوع همکاری')
    verification_code = models.ForeignKey(
        OTP, related_name='verificatio_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"


class Aboutus(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"


class Customer(models.Model):
    logo = models.ImageField(verbose_name='لوگو')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Career(models.Model):
    image = models.ImageField(verbose_name='عکس')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = "فرصت شغلی"
        verbose_name_plural = "فرصت های شغلی"
