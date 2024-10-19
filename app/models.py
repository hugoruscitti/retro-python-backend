import uuid
from django.db import models


class Proyecto(models.Model):
    hash = models.CharField(max_length=64, default="")

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

