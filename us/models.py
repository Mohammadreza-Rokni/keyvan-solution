from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

# FIELD_OF_ACTIVITY_CHOICES = [
#     ('Product', 'Product'),
#     ('Services available', 'Services available')
# ]

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
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expration_code = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Contactus(models.Model):
    # title = models.CharField(max_length=100, verbose_name='عنوان')
    # text = models.TextField(verbose_name='متن')
    full_name = models.CharField(
        max_length=200, verbose_name='نام و نام خانوادگی')
    landlineـphone = models.CharField(max_length=11, verbose_name=' تلفن ثابت')
    cellular_phone = models.CharField(
        max_length=11, verbose_name='تلفن همراه')
    email = models.EmailField(verbose_name='ایمیل')
    field_of_activity = models.CharField(
        max_length=200, verbose_name='زمینه فعالیت')
    prudoct = models.CharField(max_length=200, verbose_name='محصول / خدمات')
    state = models.CharField(
        max_length=200, verbose_name='استان')
    city = models.CharField(
        max_length=200, verbose_name='شهر')
    address = models.TextField(verbose_name='آدرس')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    # date_of_birth = models.DateField(verbose_name='تاریخ تولد')
    # degree_of_education = models.CharField(
    #     max_length=100, choices=DEGREE_OF_EDUCATION_CHOICES, verbose_name='میزان تحصیلات')
    # field_of_study = models.CharField(
    #     max_length=100, verbose_name='رشته تحصیلی')
    # skill = models.TextField(verbose_name='مهارت')
    # history = models.IntegerField(verbose_name='تجربه')
    # type_of_cooperation = models.CharField(
    #     max_length=100, choices=TYPE_OF_COOPERATION_CHOICES, verbose_name='نوع همکاری')
    verification_code = models.ForeignKey(
        OTP, related_name='verification_code', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name

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


class JobPos(models.Model):
    title = models.CharField(null=False, blank=False,
                             max_length=100, verbose_name='عنوان')
    description = models.TextField(
        null=True, blank=False, verbose_name='توضیحات')
    description_requirements = models.TextField(
        null=True, blank=True, verbose_name='نیازمندی ها')
    description_advantages = models.TextField(
        null=True, blank=True, verbose_name='مزایا')
    slug = models.SlugField(blank=True, unique=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title, allow_unicode=True)
        super(JobPos, self).save()

    class Meta:
        verbose_name = "فرصت شغلی"
        verbose_name_plural = "فرصت های شغلی"

    def get_absolute_url(self):
        return reverse('us:jobdetail', kwargs={'slug': self.slug})


class Resume(models.Model):
    job_position = models.ForeignKey(JobPos, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=False,
                             max_length=200, verbose_name='عنوان')
    resume = models.FileField(upload_to='resumes/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
