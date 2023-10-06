from django.db import models

# Create your models here.

class UsersDetail(models.Model):
    Name = models.TextField()
    Gender = models.CharField(max_length=2)
    email = models.EmailField(max_length=225)
    birth_date = models.CharField(max_length=255,default=0)
    start_date = models.DateField()

    def __str__(self):
        return self.Name
    
# class Rating(models.Model):
#     movie_title=models.CharField(max_length=255)
#     stars=models.IntegerField()

#     def __str__(self):
#         return f"{self.movie_title}: {self.stars} stars"