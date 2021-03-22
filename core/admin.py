from django.contrib import admin
from .models import Card, Syndicate, Company, Pouch

#fields -> show the fields on the register
#list_display -> show the fields on the grid
#list_filter -> filter the data by one determining by field
#search_fields -> search the data


class CardAdmin(admin.ModelAdmin):
    list_display = ('codecard', 'namecard')
    list_filter = ('namecard', )
    search_fields = ('namecard', )


class SyndicateAdmin(admin.ModelAdmin):
    list_display = ('codesynd', 'namesynd')
    list_filter = ('namesynd', )
    search_fields = ('namesynd', )


class CompanyAdmin(admin.ModelAdmin):
    fields = ('codesynd', ('codecomp', 'namecomp'))
    list_filter = ('codesynd', )
    search_fields = ('namecomp', )


class PouchAdmin(admin.ModelAdmin):
    fields = ('codepouch', ('codecard', 'codesynd', 'codecomp'), ('dtarrived', 'quant', 'value'))
    list_display = ('codepouch', 'dtarrived')
#    list_filter = ('codecard', 'codesynd', 'codecomp', 'dtarrived', )
    list_filter = ('dtarrived', )
    search_fields = ('codepouch', )


admin.site.register(Card, CardAdmin)
admin.site.register(Syndicate, SyndicateAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Pouch, PouchAdmin)

'''
admin.site.register(Card)
admin.site.register(Syndicate)
admin.site.register(Company)
admin.site.register(Pouch)
'''
