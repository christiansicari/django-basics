from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} [{self.code}]"
    
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street =  models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street} {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = 'Addresses'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    # author = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", db_index=True, unique=True)
    published_countries = models.ManyToManyField(to=Country, blank=True)

    def __str__(self):
        return f"{self.title} {self.slug}, {self.author}, {self.is_bestselling}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

