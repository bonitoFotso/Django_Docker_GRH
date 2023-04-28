from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Employer(models.Model):
    account = models.OneToOneField("User", verbose_name=("account"), on_delete=models.CASCADE)
    nom  = models.CharField(_("nom"), max_length=50)
    prenom = models.CharField(_("prenom"), max_length=50)
    tel = models.IntegerField(_("telephone"))
    tel_pro = models.IntegerField(_("tel pro"))
    ldn = models.CharField(_("lieux de naissance"), max_length=150)
    ddn = models.DateTimeField(_("date de naissance"))
    nationalite = models.CharField(_("nationalite"), max_length=50)
    est_vivant = models.BooleanField(_("est vivant"))
    sexe = models.CharField(_("sexe"), max_length=50)
    c_contact = models.IntegerField(_("contact conjoint"), null=True)
    c_nom = models.CharField(_("nom du conjoint"), max_length=50)
    C_prenom = models.CharField(_("prenom du conjoint"), max_length=50)
    nbr_enfant = models.IntegerField(_("nombre d'enfants"))
    ddmr = models.DateField(_("date de mariage"), )
    est_mr = models.BooleanField(_("est marier"))
    matrcule = models.IntegerField(_("matricune"), unique=True)
    est_valide = models.BooleanField(_("est valide"))
    
