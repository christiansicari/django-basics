from django.db import models
from django.core.validators import MinLengthValidator
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'


# Create your models here.
class Post(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(to=Tag, related_name='tags')

    def __str__(self):
        return f'{self.title} by {self.author}'



