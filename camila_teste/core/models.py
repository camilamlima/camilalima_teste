from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.


class Motorista(models.Model):
    """ model of Motoritas """

    SEXO_CHOICES = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )

    name = models.CharField(_('Nome'), max_length=200)
    birth_date = models.DateField(_('Data de Nacimento'))
    cpf = models.CharField(_('CPF'), max_length=14, unique=True)
    sexo = models.CharField(_('Sexo'), choices=SEXO_CHOICES, default='M', max_length=1)
    model_car = models.CharField(_('Modelo do carro'), max_length=200)
    active = models.BooleanField(_('Ativo'), default=True)

    def __str__(self):
        return "%s - %s " % (self.name, self.cpf)

    def get_absolute_url(self):
        return reverse('core:motorista_edit', kwargs={'pk': self.pk})


class Passageiro(models.Model):
    """ model of Passageiro """

    SEXO_CHOICES = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )

    name = models.CharField(_('Nome'), max_length=200)
    birth_date = models.DateField(_('Data de Nacimento'))
    cpf = models.CharField(_('CPF'), max_length=14, unique=True)
    sexo = models.CharField(_('Sexo'), choices=SEXO_CHOICES, default='M', max_length=1)

    def __str__(self):
        return "%s - %s " % (self.name, self.cpf)

    def get_absolute_url(self):
        return reverse('core:passageiro_edit', kwargs={'pk': self.pk})


class Corrida(models.Model):
    """ model of Coriida """

    motorista = models.ForeignKey('Motorista', on_delete=models.CASCADE)
    passageiro = models.ForeignKey('Passageiro', on_delete=models.CASCADE)
    total = models.DecimalField(_('Valor corrida'), default=0.0,
                                max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s - %s - %s" % (self.motorista, self.passageiro, self.total)
