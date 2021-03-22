from django.shortcuts import render, redirect
from .models import Card, Syndicate, Company, Pouch

from .forms import CardForm, SyndicateForm, CompanyForm, PouchForm


def index(request):
    return render(request, 'core/menu.html')


def card_list(request):
    cards = Card.objects.all()
    form = CardForm
    data = {'cards': cards, 'form': form}
    return render(request, 'core/card_list.html', data)


def card_insert(request):
    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_card_list')


def card_edit(request, id):
    card = Card.objects.get(id=id)
    form = CardForm(request.POST or None, instance=card)
    data = {}
    data['card'] = card
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_card_list')
    else:
        return render(request, 'core/card_edit.html', data)


def card_delete(request, id):
    card = Card.objects.get(id=id)
    if request.method == 'POST':
        card.delete()
        return redirect('core_card_list')
    return render(request, 'core/card_delete.html', {'obj': card})
#    return render(request, 'core/delete_confirm.html', {'obj': card})


def syndicate_list(request):
    syndicates = Syndicate.objects.all()
    form = SyndicateForm
    data = {'syndicates': syndicates, 'form': form}
    return render(request, 'core/syndicate_list.html', data)


def syndicate_insert(request):
    form = SyndicateForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_syndicate_list')


def syndicate_edit(request, id):
    syndicate = Syndicate.objects.get(id=id)
    form = SyndicateForm(request.POST or None, instance=syndicate)
    data = {}
    data['syndicate'] = syndicate
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_syndicate_list')
    else:
        return render(request, 'core/syndicate_edit.html', data)


def syndicate_delete(request, id):
    syndicate = Syndicate.objects.get(id=id)
    if request.method == 'POST':
        syndicate.delete()
        return redirect('core_syndicate_list')
    return render(request, 'core/syndicate_delete.html', {'obj': syndicate})
#    return render(request, 'core/delete_confirm.html', {'obj': syndicate})


def company_list(request):
    companys = Company.objects.all()
    form = CompanyForm
    data = {'companys': companys, 'form': form}
    return render(request, 'core/company_list.html', data)


def company_insert(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_company_list')


def company_edit(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)
    data = {}
    data['company'] = company
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_company_list')
    else:
        return render(request, 'core/company_edit.html', data)


def company_delete(request, id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        company.delete()
        return redirect('core_company_list')
    return render(request, 'core/company_delete.html', {'obj': company})
#    return render(request, 'core/delete_confirm.html', {'obj': company})


def pouch_list(request):
    pouchs = Pouch.objects.all()
    form = PouchForm
    data = {'pouchs': pouchs, 'form': form}
    return render(request, 'core/pouch_list.html', data)


def pouch_insert(request):
    form = PouchForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_pouch_list')


def pouch_edit(request, id):
    pouch = Pouch.objects.get(id=id)
    form = PouchForm(request.POST or None, instance=pouch)
    data = {}
    data['pouch'] = pouch
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_pouch_list')
    else:
        return render(request, 'core/pouch_edit.html', data)


def pouch_delete(request, id):
    pouch = Pouch.objects.get(id=id)
    if request.method == 'POST':
        pouch.delete()
        return redirect('core_pouch_list')
    return render(request, 'core/pouch_delete.html', {'obj': pouch})
#    return render(request, 'core/delete_confirm.html', {'obj': pouch})


def search(request):
    return render(request, 'core/searchReport.html')


def report(request):
#    return 'core/searchReport.html'
    return render(request, 'core/searchReport.html')


def dataanalysis(request):
#    return 'core/searchReport.html'
    return render(request, 'core/searchAnalysis.html')
