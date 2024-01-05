from django.db import models


class HomeModel(models.Model):
    photo = models.ImageField(upload_to='pages')
    discount_price = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'homes'


class AboutModel(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='pages')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductsModel(models.Model):
    photo = models.ImageField(upload_to='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ManyToManyField(CategoryModel, related_name="products")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'