from django.contrib import admin

# Register your models here.
from core.models import categoria, diretor, produtora, filme, compra, itenscompra

admin.site.register(diretor)
admin.site.register(categoria)
admin.site.register(produtora)
admin.site.register(filme)



class ItensInline(admin.TabularInline):
    model = itenscompra

@admin.register(compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)