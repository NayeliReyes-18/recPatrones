from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Paciente(models.Model):
   # name = models.CharField(max_length=50,blank=True, null=True) #Puede ser nulo
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name="Paciente"
        verbose_name_plural="Pacientes"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Paciente_detail",kwargs={"pk":self.pk})


class Tessiu(models.Model):
    temperatura = models.FloatField()
    color=models.FloatField()
    inflammation = models.FloatField(verbose_name='inflamacion')
    #name = models.CharField(max_length=50,blank=True, null=True) #Puede ser nulo
    name=models.ForeignKey(Paciente,blank=True,null=True,verbose_name="nombre",on_delete=models.CASCADE)#LLAVE FORANEA
    #FIELDNAME = models.ManyToManyField(OTHERMODEL) #RELACION MUCHOS A MUCHOS
    #OneToOneField() #RELACIÓN UNO A UNO
    
    class Meta:
       verbose_name=("Tejido")
       verbose_name_plural=("Tejidos")

    def __str__(self):
        if self.name is not None:
            return str(self.temperatura)
        else:
            return str(self.temperatura)

    def get_absolute_url(self):
        return reverse("Tejido_detail",kwargs={"pk":self.pk})