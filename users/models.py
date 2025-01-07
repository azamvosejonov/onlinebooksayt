from django.db import models
from django.contrib.auth.models import AbstractUser
from utility.models import CustomModel


class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=17,null=True,blank=True)




class Profile(CustomModel):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    avatar=models.ImageField(upload_to='user_avatar/',null=True,blank=True)


    def __str__(self):
        return self.user.username
