from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories'
    )
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narx
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0) # Chegirma foizda (%) beriladi

    def final_price(self):
        """Chegirmali narxni hisoblash"""
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.product.name} - Rating: {self.rating}"




from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
