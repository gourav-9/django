from django.db import models
     
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=2000,default='Default description')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
     