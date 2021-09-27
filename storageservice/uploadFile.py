import boto3
from botocore.exceptions import NoCredentialsError
import requests
import mimetypes


ACCESS_KEY_ID = 'AKIATTRKRHB27MBZFS5X'
SECRET_ACCESS_KEY = '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'

def upload_file(remote_url, bucket, file_name):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    try:
        imageResponse = requests.get(remote_url, stream=True).raw
        content_type = imageResponse.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        s3.upload_fileobj(imageResponse, bucket, file_name + extension)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False



#ejemplo peticion
def uploadImage():

    url = "http://127.0.0.1:8081/uploadimage/usuarios"

    archivo={'media': open('/home/seed/Imágenes/andugay.png', 'rb')}
    headers = {
        'Cookie': 'csrftoken=94iHNosxOaWYDo1nVVwT71yq8XV9gcp3wN9fKJTLsj8kxIffoq6sLJkCKT0yDMS4'
    }
    response = requests.request("POST", url, headers=headers,  files=archivo)

    print(response.text)

#uploaded = upload_file('https://i2.wp.com/unaaldia.hispasec.com/wp-content/uploads/2013/09/f4b65-django-logo.png?ssl=1', 'seedpay-bucket', 'imgDos')

uploadImage()