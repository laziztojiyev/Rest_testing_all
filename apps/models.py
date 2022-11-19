from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        db_table = 'categories'
        ordering = ('-created_at', )


class Product(BaseModel):
    class Size(models.TextChoices):
        S = 'S'
        L = 'L'
        XL = 'XL'
        XXL = 'XXL'

    class Color(models.TextChoices):
        Black = 'Black'
        Red = 'RED'
        BLUE = 'BLUE'
        GREEN = 'GREEN'
        WHITE = 'WHITE'
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=9, decimal_places=2, default=30000)
    description = models.TextField()
    size = models.CharField(max_length=25, choices=Size.choices, default=Size.S)
    color = models.CharField(max_length=25, choices=Color.choices, default=Color.WHITE)
    expired_date = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, CASCADE, 'category')

    @property
    def product_images(self):
        return self.product_images.all()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        ordering = ('-created_at', )


class ProductImages(BaseModel):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, CASCADE, 'product_images')

    class Meta:
        db_table = 'images'




