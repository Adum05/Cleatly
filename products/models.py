from django.db import models

class Product(models.Model):
    STUD_TYPE = [
        ('FG', 'Firm Ground'),
        ('AG', 'Artificial Ground'),
        ('TF', 'Turf'),
    ]

    prod_name = models.CharField(max_length= 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank= True, null= True)
    stock = models.IntegerField(default=0)
    Cleat_stud = models.CharField(max_length=2, choices=STUD_TYPE, default='FG')

    def __str__(self):
        return self.prod_name