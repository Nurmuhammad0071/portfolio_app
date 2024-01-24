from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=0)


# Create your models here.
class MyInfo(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.FileField(upload_to='images')
    text = models.CharField(max_length=255)
    birthday = models.DateField(default=timezone.now)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    degree = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    freelance = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    map = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Site(BaseModel):
    about_title = models.CharField(max_length=255)
    happy_clients = models.IntegerField()
    projects = models.IntegerField()
    support = models.IntegerField()
    workers = models.IntegerField()

    def __str__(self):
        return self.about_title


class Experience(BaseModel):
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField(max_length=255, )
    finished = models.DateField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skill(BaseModel):
    name = models.CharField(max_length=255)
    knowledge = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Summary(BaseModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class PortfolioImage(BaseModel):
    image = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return "Image"


class Portfolio(BaseModel):
    image = models.ManyToManyField(PortfolioImage, blank=True)
    name = models.CharField(max_length=255)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    client = models.CharField(max_length=255)
    project_date = models.DateTimeField(default=timezone.now)
    project_url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Testimonial(BaseModel):
    image = models.ImageField(upload_to='portfolio')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(BaseModel):
    your_name = models.ImageField(upload_to='portfolio')
    your_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.your_name
