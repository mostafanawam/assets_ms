from django.db import models


#  python manage.py dumpdata auth.User --output main/fixtures/User.static.json



#  python manage.py dumpdata main.Asset --output main/fixtures/Asset.test.json
class Asset(models.Model):
    ASSET_STATUS = (
        ('available', 'Available'),
        ('lent', 'Lent Out')
    )
    ASSET_CATEGORY = (
        ('electronics', 'Electronics'),
        ('office', 'Office Supplies')
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=ASSET_CATEGORY)
    status = models.CharField(max_length=20, choices=ASSET_STATUS, default='available')
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    @property
    def current_lending(self):
        """
        Returns the current lending instance if the asset is lent out, otherwise None.
        """
        return Lending.objects.filter(asset=self, return_date__isnull=True).first()

    @property
    def is_lent(self):
        """
        Returns True if the asset is currently lent out, False otherwise.
        """
        return self.current_lending is not None
    
    @property
    def current_employee(self):
        """
        Returns the employee who currently holds the asset, if it is lent out.
        """
        lending = self.current_lending
        return lending.employee if lending else None
    
    def __str__(self):
        return f"{self.name}"

#  python manage.py dumpdata main.Employee --output main/fixtures/Employee.test.json
class Employee(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class Lending(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    lend_date = models.DateTimeField(auto_now_add=True)
    # expected_return_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.asset.name} lent to {self.employee.name}"

    class Meta:
        # Ensure that an asset can't be lent out to multiple employees at the same time
        constraints = [
            models.CheckConstraint(
                check=models.Q(return_date__isnull=True) | models.Q(return_date__isnull=False),
                name='asset_return_check'
            ),
        ]
        # Indexes for faster querying on common filters
        indexes = [
            models.Index(fields=['return_date']),
            models.Index(fields=['lend_date']),
        ]