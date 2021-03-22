from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


def date_valid(data) -> bool:
    try:
        # datetime.strptime(data, 'YYYY-mm-dd')
        datetime.strftime(data, 'YYYY-mm-dd')
        return True
    except ValueError:
        return False


class Card(models.Model):
    codecard = models.IntegerField(unique=True)
    namecard = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.namecard


class Syndicate(models.Model):
    codesynd = models.IntegerField(unique=True)
    namesynd = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.namesynd


class Company(models.Model):
    codesynd = models.ForeignKey(Syndicate, on_delete=models.CASCADE)
    codecomp = models.IntegerField(blank=False, null=False)
    namecomp = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.namecomp


def verify_date(value):
    if date_valid(value):
        # if datetime.strptime(self.dtarrived, '%d/%m/%Y').date() > datetime.now().date():
        if value > datetime.now().date():
            raise ValidationError('Date arrived is bigger actual date')
    else:
        raise ValidationError('Invalid Date Arrived')


class Pouch(models.Model):
    codepouch = models.CharField(max_length=10, blank=False, null=False)
    codecard = models.ForeignKey(Card, blank=False, null=False, on_delete=models.CASCADE)
    codesynd = models.ForeignKey(Syndicate, blank=False, null=False, on_delete=models.CASCADE)
    codecomp = models.ForeignKey(Company, blank=False, null=False, on_delete=models.CASCADE)
    dtarrived = models.DateField(blank=False, null=False, validators=[verify_date])
    quant = models.IntegerField(blank=False, null=False)
    value = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.codepouch
