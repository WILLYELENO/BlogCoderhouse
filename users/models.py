from django.contrib.auth.models import AbstractUser

# Create your models here.

#Usuario customizado:


class User (AbstractUser):
    

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'