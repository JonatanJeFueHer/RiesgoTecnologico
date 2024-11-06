from django.contrib import admin
from .models import Usuario
from .models import Administrador
from .models import Anuncio
from .models import AnuncioContra

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Anuncio)
admin.site.register(AnuncioContra)