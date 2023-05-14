from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=256, verbose_name='상품명')
    price=models.IntegerField(verbose_name="상품가격")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description=models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고")
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'my_product'
        verbose_name = '상품'
        verbose_name_plural='상품'

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.id])