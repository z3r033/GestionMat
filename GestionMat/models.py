from django.db import models

# Create your models here.
from decimal import Decimal
from django.core.validators import MinValueValidator


# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class MaterialManager(models.Manager):
 def get_queryset(self):
  return super(MaterialManager,self).get_queryset().filter(editeur='hayat')

class material(models.Model):
 def get_absolute_url(self):
  return reverse('GestionMat:material_detail',
                 args=[self.publish.year,self.numero_serie])
 def get_delete_url(self):
  return reverse('GestionMat:delete',
                 args=[self.numero_serie])
 def get_update_url(self):
  return reverse('GestionMat:update',
                 args=[self.numero_serie])
 MAINTENANCE_CHOICES = (
 (True, "Oui"),
 (False, "Non"),
 )
 numero_serie = models.CharField(max_length=10,unique=True)
 date_achat = models.DateField(auto_now=False,auto_now_add=False)
 garantie_duree= models.IntegerField(validators=[MinValueValidator(0)])
 achat_lieu=models.CharField(max_length=50)
 achat_prix=models.DecimalField(max_digits=9, decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))])
 marque=models.CharField(max_length=80)
 date_derniere_maintenance=models.DateField(auto_now=False,auto_now_add=False)
 contrat_maintenance= models.BooleanField(choices=MAINTENANCE_CHOICES)
 duree= models.IntegerField(validators=[MinValueValidator(0)],null=True,blank=True)
 lieu_affectation=models.CharField(max_length=100)
 editeur = models.ForeignKey(User,
 on_delete=models.SET_NULL,
 related_name='materials',
 null=True)

 publish = models.DateTimeField(default=timezone.now)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)
 objects=models.Manager()
 mat=MaterialManager()

 class Meta:
    ordering = ('-publish',)

 def __str__(self):
     return self.numero_serie+" "+self.marque