from .informVentaGeneralSerializer import *
from django.db.models import Count, Sum, F
from calendar import monthrange
from datetime import datetime
from dateutil.parser import parse

class ManejadorInformeVentasGeneral():

    def ejecutar(self, peticion):
        negocios = negocio.objects.filter(usuario = peticion['usuario'].id)
        fecha_inicio = datetime.strptime("%d-%d-01"%(peticion['año'],peticion['mes']), '%Y-%m-%d')
        fecha_fin = datetime.strptime("%d-%d-%s"%(peticion['año'],peticion['mes'], str(monthrange(peticion['año'], peticion['mes'])[1])), '%Y-%m-%d')
        
        infomeGeneral = {'negocios': []}

        for negocioAux in negocios:
            productosFacturas = factura_producto.objects.filter(factura__negocio = negocioAux.id, factura__fecha_creacion__gte = fecha_inicio,
                                factura__fecha_creacion__lte = fecha_fin ).values('producto__nombre').order_by('producto').annotate(
                                    unidadesVendidas=Sum('cantidad'),
                                    valorTotal=F('unidadesVendidas')*F('producto__precio'),
                                    producto = F('producto__nombre'))

            infoNegocio={'negocio':negocioAux,
                        'productos': productosFacturas,
                        'total': sum([vt['valorTotal'] for vt in productosFacturas]) }

            infomeGeneral['negocios'].append(infoNegocio)

        infomeGeneral['total'] = sum([ng['total'] for ng in infomeGeneral['negocios']])
        print("info negocio : ", infomeGeneral)
        
        return InformeVentasGeneralSerializer(infomeGeneral).data
