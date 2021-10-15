from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import qrcode
import io
from ..models import negocio
from django.http import HttpResponse

class QrView(APIView):

    def get(self, request, id, *args, **kwargs):
        urlcatalogo = 'http://127.0.0.1:4200/catalogo/'
        if negocio.objects.filter(pk = id).exists():
            #Creating an instance of qrcode
            urlcatalogo =  urlcatalogo + str(id)
            
            qr = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
            qr.add_data(urlcatalogo)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = io.BytesIO()
            img.save(buffer)

            response = HttpResponse(buffer.getbuffer())
            response['Content-Type'] = "image/png"
            response['Cache-Control'] = "max-age=0"
            return response
        else:
            return Response("Negocio incorrecto", status=status.HTTP_404_NOT_FOUND)

