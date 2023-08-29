from django.db import models

# Create your models here.

class Details(models.Model):
    
    book_name = models.CharField(max_length=250,default="unknown")
    book_author = models.CharField(max_length=200,default="True")
    no_of_pages = models.IntegerField()
    publish_date = models.DateField(auto_now=True)
    email_id = models.EmailField("mno@gmail.com")
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name