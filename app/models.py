import uuid
from django.db import models
from django.utils import timezone


class Proyecto(models.Model):
    hash = models.CharField(max_length=64, default="")
    fecha = models.DateTimeField(default=timezone.now)
    screenshot = models.TextField(blank=True)
    codigo = models.TextField(blank=True)
    textura = models.TextField(blank=True)
    version = models.CharField(blank=True, max_length=16)

    class Meta:
        ordering = ['-id']
        db_table = 'proyectos'
        verbose_name_plural = "proyectos"

    def __str__(self):
        return self.hash

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = uuid.uuid4()

        super(Proyecto, self).save(*args, **kwargs)

