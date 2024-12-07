from django.db import models

# Create your models here.


class Movie(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    price=models.IntegerField(default=100)
    
    
    def __str__(self):
        return str(self.id)+"_"+self.title
    
class Order(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateTimeField(auto_now=True)
    total=models.IntegerField(default=123)
    def __str__(self) -> str:
        return str(self.id)+str(self.date)
    
class Item(models.Model):
    id=models.AutoField(primary_key=True)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.id)+" : "+self.movie.title