import boto3
from django.http import JsonResponse
from botocore.exceptions import NoCredentialsError
from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.conf import settings
import uuid



class FileUploadView(views.APIView):
    parser_classes = [ MultiPartParser]

    def post(self, request, typeImage, format=None):
        file_obj = request.data['media']
        contentype = file_obj.name.split('.')[1]
        s3 = boto3.client('s3', aws_access_key_id=settings.ACCESS_KEY_ID, aws_secret_access_key=settings.SECRET_ACCESS_KEY)
    
        try:
            filename = "%s/%s.%s"%(typeImage,uuid.uuid4(),contentype)

            s3.upload_fileobj(file_obj, settings.BUCKET_IMAGENES, filename , ExtraArgs={'ACL': 'public-read'})

            return JsonResponse({'urlImagen': filename})

        except FileNotFoundError as error:
            return Response({'error': str(error)}, status=404)
        except NoCredentialsError as error:
            return Response({'error': str(error)}, status=404)






    