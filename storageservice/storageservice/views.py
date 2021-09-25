import boto3
from django.http import JsonResponse
from botocore.exceptions import NoCredentialsError
import requests
import mimetypes

ACCESS_KEY_ID = 'AKIA6CKUFVDMBKWKTXE2'
SECRET_ACCESS_KEY = '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'
BUCKET_NAME ='seedpaybuck'


def guardarImagenEnS3(response):

    fileImg =  response.FILES


    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    
    try:
        imagen = 'https://i2.wp.com/unaaldia.hispasec.com/wp-content/uploads/2013/09/f4b65-django-logo.png?ssl=1'

        imageResponse = requests.get(imagen, stream=True).raw
        print("Upload Successful : " + str(s3.upload_fileobj(imageResponse, BUCKET_NAME, 'asdas.png')))
        file_object = s3.ObjectAcl(BUCKET_NAME, 'asdas.png')
        return JsonResponse({'urlimagen': str(file_object.put(ACL = 'public-read')) })

    except FileNotFoundError as error:
        print("The file was not found")
        return JsonResponse({'error': str(error)})
    except NoCredentialsError as error:
        print("Credentials not available")
        return JsonResponse({'error': str(error)})
    