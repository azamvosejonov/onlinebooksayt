from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.utils.text import slugify
from utility.models import CustomModel
from users.models import CustomUser

class Author(CustomModel):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=150)
    bio=models.TextField(null=True,blank=True)
    birth_day=models.DateField(null=True,blank=True)
    death_date=models.DateField(null=True,blank=True)
    web_site=models.URLField(null=True,blank=True)
    author_avatar=models.ImageField(null=True,blank=True,upload_to="author_avatar/")

    def __str__(self):
        return self.first_name


class Publisher(CustomModel):
    name=models.CharField(max_length=150)
    address=models.TextField()
    web_site=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Category(CustomModel):
    name=models.CharField(max_length=150,unique=True,null=False,blank=False)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Book(CustomModel):
    title=models.CharField(max_length=250)
    slug=models.SlugField(unique=True,max_length=250)
    category=models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default="Nomalum")
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,blank=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.SET_NULL,null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    last_price=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    cover_pic=models.ImageField(upload_to="book_image/",null=True,blank=True)
    ebook=models.FileField(upload_to="ebook/",null=True,blank=True)
    audio_book=models.FileField(upload_to="audio_book/",null=True,blank=True)
    description=models.TextField()
    stock=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)

        super().save(*args,**kwargs)


class Review(CustomModel):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="reviews")
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="reviews")
    comment=models.TextField()
    rate=models.ImageField(
        validators=[
            MinValueValidator(1,message="1 dan kichik son kiriting!"),
            MaxValueValidator(5,message="5 dan katta son kiriting!"),

        ]
    )

    def __str__(self):
        return f"{self.user} {self.book} {self.rate}"



