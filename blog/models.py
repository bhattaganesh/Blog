from django.db import models
status = (('public','Public'),('draft','Draft'))

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.title

class  Post(models.Model):  
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=6,choices=status,default=status[0][0])
    def __str__(self):
            return self.title
    class Meta:
        db_table = 'post'