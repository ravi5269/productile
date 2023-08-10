from django.db import models


class Category(models.Model):
    # id = models.ForeignKey(unique=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    # id = models.ForeignKey(unique=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_image/")
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name
