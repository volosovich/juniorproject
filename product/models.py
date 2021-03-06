from django.db import models

class Category(models.Model):
    
    name = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True) 
    modified_at = models.DateTimeField(auto_now = True)
    category_for_product = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
