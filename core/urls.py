from django.urls import path
from .views import (index, card_list, card_insert, card_edit, card_delete,
                    syndicate_list, syndicate_insert, syndicate_edit, syndicate_delete,
                    company_list, company_insert, company_edit, company_delete,
                    pouch_list, pouch_insert, pouch_edit, pouch_delete,
                    search, report, dataanalysis)


urlpatterns = [
    path('', index, name='index'),

    path('cards/', card_list, name='core_card_list'),
    path('card_insert/', card_insert, name='core_card_insert'),
    path('card_edit/<int:id>/', card_edit, name='core_card_edit'),
    path('card_delete/<int:id>/', card_delete, name='core_card_delete'),

    path('syndicates/', syndicate_list, name='core_syndicate_list'),
    path('syndicate_insert/', syndicate_insert, name='core_syndicate_insert'),
    path('syndicate_edit/<int:id>/', syndicate_edit, name='core_syndicate_edit'),
    path('syndicate_delete/<int:id>/', syndicate_delete, name='core_syndicate_delete'),

    path('companys/', company_list, name='core_company_list'),
    path('company_insert', company_insert, name='core_company_insert'),
    path('company_edit/<int:id>/', company_edit, name='core_company_edit'),
    path('company_delete/<int:id>/', company_delete, name='core_company_delete'),

    path('pouchs/', pouch_list, name='core_pouch_list'),
    path('pouch_insert', pouch_insert, name='core_pouch_insert'),
    path('pouch_edit/<int:id>/', pouch_edit, name='core_pouch_edit'),
    path('pouch_delete/<int:id>/', pouch_delete, name='core_pouch_delete'),

    path('search/', search, name='core_search'),
    path('report/', report, name='core_report'),
    path('dataanalysis/', dataanalysis, name='core_dataanalysis'),
]
