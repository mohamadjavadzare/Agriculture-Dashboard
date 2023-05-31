from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=90)
    phone = models.IntegerField()
    status = models.BooleanField(default=False)
    last_employed = models.DateField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)
        verbose_name = ("کارگر")
        verbose_name_plural = ("کارگران")
    def __str__(self):
        return "{} - {}".format(self.name, self.id)
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Worker)
    budget = models.CharField(max_length=100)
    completion = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)
        verbose_name = ("پروژه")
        verbose_name_plural = ("پروژه ها")

    def __str__(self):
        return "{} - {}".format(self.name, self.id)
    

class ProductStatus(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("وضعیت محصول")
        verbose_name_plural = ("وضعیت محصولات")
    def __str__(self):
        return "{}".format(self.name)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/', default='product/default.png')
    completion = models.PositiveIntegerField(default=0)
    status = models.ForeignKey(ProductStatus, on_delete=models.PROTECT)
    budget = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        verbose_name = ("محصول")
        verbose_name_plural = ("محصولات")

    def __str__(self):
        return "{} - {}".format(self.name, self.id)
    