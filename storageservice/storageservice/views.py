import boto3
from django.http import JsonResponse
from botocore.exceptions import NoCredentialsError
import requests
import mimetypes
from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import uuid



class FileUploadView(views.APIView):
    parser_classes = [ MultiPartParser]

    def post(self, request, typeImage, format=None):
        file_obj = request.data['media']
        contentype = file_obj.name.split('.')[1]
        print("info data : " + str(request.data) + '  content type : ' + str(contentype))

        s3 = boto3.client('s3', aws_access_key_id=settings.ACCESS_KEY_ID, aws_secret_access_key=settings.SECRET_ACCESS_KEY)
    
        try:
            filename = uuid.uuid4()
            print("name file : " + str(filename))
            url = s3.upload_fileobj(file_obj, settings.BUCKET_IMAGENES, typeImage + '/' + str(filename) + contentype, ExtraArgs={'ACL': 'public-read'})

            return JsonResponse({'urlImagen': str(url)})

        except FileNotFoundError as error:
            print("The file was not found")
            return JsonResponse({'error': str(error)})
        except NoCredentialsError as error:
            print("Credentials not available")
            return JsonResponse({'error': str(error)})






    