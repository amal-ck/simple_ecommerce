from django.db import models

# Create your models here.
class ShoppingItems(models.Model):
    item_name = models.CharField(max_length =200,null=True)
    item_desc = models.TextField(null=True)
    item_img = models.ImageField(upload_to='item_image', null=True)
    item_price = models.DecimalField(max_digits=10,decimal_places=2,null=True)

    def __str__(self):
        return self.item_name