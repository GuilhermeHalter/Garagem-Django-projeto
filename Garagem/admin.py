from django.contrib import admin


from Garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo

admin.site.register(Acessorio)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Marca)
admin.site.register(Veiculo)
# Register your models here.
