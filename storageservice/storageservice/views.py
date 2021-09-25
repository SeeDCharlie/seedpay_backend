import boto3
from django.http import JsonResponse
from botocore.exceptions import NoCredentialsError
import requests
import mimetypes
from django.views.decorators.csrf import csrf_exempt

ACCESS_KEY_ID = 'AKIA6CKUFVDMBKWKTXE2'
SECRET_ACCESS_KEY = '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'
BUCKET_NAME ='seedpaybuck'


@csrf_exempt
def guardarImagenEnS3(request):
    fileImg = []
    for filename, file in request.FILES.iteritems():
        fileImg.append(filename)
    print(fileImg)
    return JsonResponse({'msj' : 'nadaaa!!'})

# def guardarImagenEnS3(response):

#     fileImg =  response.FILES


#     s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    
#     try:
#         imagen = 'https://i2.wp.com/unaaldia.hispasec.com/wp-content/uploads/2013/09/f4b65-django-logo.png?ssl=1'

#         imageResponse = requests.get(imagen, stream=True).raw
#         url = s3.upload_fileobj(imageResponse, BUCKET_NAME, 'asdas.png', ExtraArgs={'ACL': 'public-read'})

#         return JsonResponse({'urlimagen': str(url)})

#     except FileNotFoundError as error:
#         print("The file was not found")
#         return JsonResponse({'error': str(error)})
#     except NoCredentialsError as error:
#         print("Credentials not available")
#         return JsonResponse({'error': str(error)})
    