from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length= 255)
    logo = models.ImageField(upload_to='Cars/logo/')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Brand"


class Car(models.Model):
    ENGINE_TYPES = (
        ("BENZIN","BENZIN"),
        ("ELEKTR","ELEKTR"),
        ("GIBRID","GIBRID")
    )
    name = models.CharField(max_length= 255)
    image = models.ImageField(upload_to='Cars/')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    time = models.FloatField()
    power = models.IntegerField()
    speed = models.IntegerField()
    engine = models.CharField(max_length=50, choices=ENGINE_TYPES,
                            default="BENZIN")
    price = models.IntegerField()
        
    def __str__(self) -> str:
        return f"{self.brand} | {self.name}"
    
    class Meta:
        verbose_name_plural = "Car"
        
    
