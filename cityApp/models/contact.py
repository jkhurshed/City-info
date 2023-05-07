from django.db import models

class Contact(models.Model):

    phone = models.CharField("Номер телефона", max_length=12)
    additionalPhone = models.CharField("Дополнительный номер телефона", max_length=12, null=True)
    work_routine = models.CharField("График работы", max_length=50)
    email = models.EmailField("Почта", max_length=50)
    image = models.ImageField(upload_to="images/")

    place = models.OneToOneField("cityApp.place", on_delete=models.CASCADE, related_name="contact")

    class Meta:
        
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
    def __str__(self) -> str:
        return f"Контакты {self.place}"