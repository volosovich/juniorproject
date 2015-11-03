from django.db import models


class TestforPage(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    
    name = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField()


    def __unicode__(self):
        return self.name
        return self.description
        return self.slug

class Product(models.Model):

    name = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add = True) 
    modified_at = models.DateField(auto_now = True)
    category_for_product = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
        return self.description
        return self.slug
        return self.price
        return self.created_at
        return self.modified_at

