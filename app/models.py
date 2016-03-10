from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
    """
    Customers class model
    """
    customer_id = models.CharField(max_length=15)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15 ,blank=True)
    address = models.TextField()
    registered_date = models.DateTimeField(blank=True, null=True)

    STATUS_CHOICES = (
        (0, 'Not Verified'),
        (1, 'Verified'),
        (2, 'Not Trusted')
        )
    validation = models.IntegerField(choices=STATUS_CHOICES, default=0)
    #validation = models.CharField(max_length=20, default="Not Verified")

    def register(self):
        self.registered_date = timezone.now().date()
        self.save()

    def not_verified(self):
        self.validation = 0
        self.save()

    def Verified(self):
        self.validation = 1
        self.save()

    def not_trusted(self):
        self.validation = 2
        self.save()


    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    full_name = property(__str__)


class Category(models.Model):
    """
    Category class model
    """
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/category', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    def register(self):
        self.created_at = timezone.now()
        self.modified_at = self.created_at
        self.save()

    def modify(self):
        self.modified_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product class model
    """
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='images/products', blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)


    def register(self):
        self.created_at = timezone.now()
        self.modified_at = self.created_at
        self.save()

    def modify(self):
        self.modified_at = timezone.now()
        self.save()
            
    def __str__(self):
        return self.name