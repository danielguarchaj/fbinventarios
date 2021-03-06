from django.contrib import admin

from .models import (
    Agencia,
    Cliente,
    Producto,
    EntregaArticuloPromocional,
)

admin.site.register(Agencia)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(EntregaArticuloPromocional)