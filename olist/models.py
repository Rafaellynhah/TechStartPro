from django.db import models


class Category(models.Model):
    name = models.CharField(max_length= 50)

    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name    


class Product(models.Model):
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length=100)
    value = models.FloatField()
    category = models.ManyToManyField(Category)


    class Meta:
        db_table = "product"        


class Concat(models.Aggregate):
    function = 'group_concat'
    template = '%(function)s(%(field)s, "%(separator)s")'

