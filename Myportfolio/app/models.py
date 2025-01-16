from django.db import models


# Create your models here.
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Person(SingletonModel):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, null=True)
    com_projects = models.IntegerField(null=True)
    awards = models.IntegerField(null=True)
    happy_customer = models.IntegerField(null=True)
    coffee_cup = models.IntegerField(null=True)
    website = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    image1 = models.ImageField(upload_to='portfolio/images/')
    image2 = models.ImageField(upload_to='portfolio/images/')
    document = models.FileField(upload_to='portfolio/documents/')

    def __str__(self):
        return self.name


class Background(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    duration = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']

class Projects(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
