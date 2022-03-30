from django.db import models
from email.policy import default
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=True, blank=True)

    

    def __str__(self):
        return self.category_name


class Nomination(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    index = models.IntegerField(blank=True, null=True)
    link = models.URLField()
    picture = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    

class Vote(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    nomination = models.ForeignKey(Nomination, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    request_obj = models.TextField(null=True, blank=True)
    ipaddress = models.CharField(max_length=12, null=True, blank=True)
    
    def __str__(self):
        return str(self.category)



class Timestamps(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
  
    class Meta:
        abstract = True