from django.forms import ModelForm
from .models import Card, Syndicate, Company, Pouch


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


class SyndicateForm(ModelForm):
    class Meta:
        model = Syndicate
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class PouchForm(ModelForm):
    class Meta:
        model = Pouch
        fields = '__all__'
