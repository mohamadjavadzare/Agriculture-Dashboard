from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='worker/', default='worker/default.png')
    skill = models.CharField(max_length=100, default='کارگر ساده')
    salary = models.CharField(max_length=100, default='350000 Toman')
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
    completion = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
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
    completion = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
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

class ToolsStatus(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("وضعیت ابزار")
        verbose_name_plural = ("وضعیت ابزارآلات")
    def __str__(self):
        return "{}".format(self.name)
    
class Tools(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tools/', default='tools/machine.png')
    number = models.IntegerField(default=0)
    status = models.ForeignKey(ToolsStatus , on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        verbose_name = ("ابزار")
        verbose_name_plural = ("ابزارآلات")

    def __str__(self):
        return "{} - {}".format(self.name, self.id)
    
class Card(models.Model):
    name = models.CharField(max_length=60)
    card_number = models.PositiveBigIntegerField(null=False, default=0)
    image = models.ImageField(upload_to='card/', default='card/mastercard.png.png')
    budget = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        verbose_name = ("کارت بانکی")
        verbose_name_plural = ("کارت های بانکی")

    def __str__(self):
        return "{} - {}".format(self.name, self.id)