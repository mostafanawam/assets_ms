from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


#  python manage.py dumpdata auth.User --output main/fixtures/User.static.json



class Asset(models.Model):
    ASSET_STATUS = (
        ('available', 'Available'),
        ('lent', 'Lent Out'),
        # ('maintenance', 'Under Maintenance'),
        # ('retired', 'Retired'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)  # e.g., 'Laptop', 'Vehicle', 'Furniture'
    # purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=ASSET_STATUS, default='available')
    # serial_number = models.CharField(max_length=100, unique=True)
    # location = models.CharField(max_length=100)  # e.g., 'Office A', 'Storage Room'
    
    def __str__(self):
        return f"{self.name}"




    
class Lending(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    lend_date = models.DateTimeField(default=timezone.now)
    # expected_return_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)

    # def is_overdue(self):
    #     if self.actual_return_date:
    #         return False
    #     return timezone.now() > self.expected_return_date
    
    def __str__(self):
        return f"{self.asset.name} lent to {self.employee.user.username}"