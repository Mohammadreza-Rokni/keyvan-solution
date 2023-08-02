from django.db import models


# Create your models here.


fieldـofـactivity_list = [
  ('product', 'product'),
  ('services available', 'Services available')
]

degreeـofـeducation_list = [ 
  ('Diploma', 'Diploma'),
  ('Associate', 'Associate'),
  ('Bachelor', 'Bachelor'),
  ('Master', 'Master'),
  ('Doctorate', 'Doctorate')
]

type_of_cooperation_list = [
  ('Full-time', 'Full-time'),
  ('Part-time', 'Part-time'),
  ('Project', 'Project')
]


class Contactus(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  created = models.DateTimeField()
  full_name = models.CharField(max_length=200)
  phone_number = models.IntegerField(max_length=12)
  fieldـofـactivity = fieldـofـactivity_list
  activityـprovince = models.CharField(max_length=100)
  date_of_birth = models.DateField()
  degreeـofـeducation = degreeـofـeducation_list
  field_of_Study = models.CharField(max_length=100)
  skill = models.TextField()
  history = models.IntegerField()
  type_of_cooperation = type_of_cooperation_list

  def __str__(self):
    return self.title

class Aboutus(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField()

  class Meta:
        verbose_name = "درباره ما"

class Customer(models.Model):
  logo = models.ImageField()
  title = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
        return self.title
  
  class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"