from django.db import models

class Bandas(models.Model):
    id = models.AutoField(primary_key=True)
    banda = models.CharField("nome", max_length=60)

    def __str__(self) -> str:
        return self.banda
    
    class Meta:
        verbose_name = "Banda"
        verbose_name_plural = "Bandas"

class Albuns(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("titulo", max_length=30)
    Banda = models.ForeignKey(Bandas, on_delete=models.PROTECT)
    data = models.DateField("data")

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albuns"

class Musicas(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("titulo", max_length=30)
    segundos = models.IntegerField("segundos", default=0)
    album = models.ForeignKey(Albuns, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = "Musica"
        verbose_name_plural = "Musicas"
        