from django.db import models

class Misurazione(models.Model):

    lunghezza = models.IntegerField(default=0)

    misurazione1 = models.DecimalField(max_digits=4, decimal_places=2)
    misurazione2 = models.DecimalField(max_digits=4, decimal_places=2)
    misurazione3 = models.DecimalField(max_digits=4, decimal_places=2)

    media = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True, null=True)
    errore = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.lunghezza)

    def salva(self):
        self.media = float(self.misurazione1 + self.misurazione2 + self.misurazione3) / 3.0
        self.errore = float(max([self.misurazione1, self.misurazione2, self.misurazione3]) - min([self.misurazione1, self.misurazione2, self.misurazione3])) / 2.0

class Esperimento(models.Model):

    name = models.CharField(max_length=100)

    es1 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es1")
    es2 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es2")
    es3 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es3")
    es4 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es4")
    es5 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es5")
    es6 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es6")
    es7 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es7")
    es8 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es8")
    es9 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es9")
    es10 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es10")
    es11 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es11")
    es12 = models.ForeignKey('Misurazione', on_delete=models.CASCADE, related_name="es12")

    def __str__(self):
        return self.name
