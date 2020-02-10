from django.db import models
from django.urls import reverse

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=40)
    credit_score = models.IntegerField()
    geography = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    tenure = models.IntegerField()
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    num_of_products = models.IntegerField()
    has_credit_card = models.BooleanField()
    is_active_member = models.BooleanField()
    estimated_salary = models.DecimalField(decimal_places=2, max_digits=10)
    exited = models.BooleanField()

    def __str__(self):
        return self.client_name
    # 
    # def get_absolute_url(self):
    #     return reverse('client-detail', kwargs={'pk':self.pk})
