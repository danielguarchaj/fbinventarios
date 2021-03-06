from django.db import models

# class Producto(models.Model):
#     nombre = models.CharField(max_length=250)
#     codigo = models.CharField(max_length=250)
#     descripcion = models.TextField()
#     imagen = models.ImageField(upload_to='media/productos/', null=True, blank=True)
#     stock = models.IntegerField(default=0)
#     stock_max = models.IntegerField()
#     existencia_total = models.DecimalField(decimal_places=2, max_digits=13)
#     precio_compra = models.DecimalField(decimal_places=2, max_digits=13)
#     precio_venta = models.DecimalField(decimal_places=2, max_digits=13)
#     ventas = models.IntegerField()
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     descripcion_larga = models.TextField()
#     estado = models.SmallIntegerField(default=1)

#     categoria = models.ForeignKey(ProductoCategoria, on_delete=models.CASCADE, related_name='categoria_productos')
#     ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='ubicacion_productos')
#     unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, related_name='unidad_medida_productos')

class Agencia(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return f'Codigo: {self.pk} - Nombre: {self.nombre}'

    class Meta:
        verbose_name = 'Agencia'
        verbose_name_plural = 'Agencias'


class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    segmento = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)
    ciclo_credito = models.IntegerField()

    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    cliente_que_refiere = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    es_referido = models.BooleanField()
    
    def __str__(self):
        return f'Codigo: {self.pk} - Nombre: {self.nombre} - Es referido: {self.es_referido}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    existencias = models.IntegerField()

    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Codigo: {self.pk} - Nombre: {self.nombre}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class EntregaArticuloPromocional(models.Model):
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Codigo: {self.pk} - Descripcion: {self.descripcion}'

    class Meta:
        verbose_name = 'Entrega de Articulo Promocional'
        verbose_name_plural = 'Entregas de Articulos Promocionales'

