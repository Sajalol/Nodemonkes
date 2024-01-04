from django.db import models
from django.contrib.auth.models import User

class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    traits = models.ManyToManyField(Trait)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listed_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)  # Optional: URL to the NFT image
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Optional: Link to the user who listed the NFT

    def __str__(self):
        return self.title

class Sale(models.Model):
    traits = models.ManyToManyField(Trait)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)  # Adjusted max_digits and decimal_places
    sale_date = models.DateTimeField()
    pending_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"Sale of {', '.join([trait.name for trait in self.traits.all()])} on {self.sale_date.strftime('%d-%m-%y')}"





