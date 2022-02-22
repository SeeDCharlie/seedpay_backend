sudo yum -y install epel-release
sudo yum -y update
sudo yum groupinstall "Development Tools" -y
sudo yum install openssl-devel libffi-devel bzip2-devel -y
wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
tar xvf Python-3.9.10.tgz
cd Python-3.9*/
./configure --enable-optimizations
sudo make altinstall

export SECRET_KEY="django-insecure-#j6@qz@@)!$26stcznj24da(fe-+xneirc47_(olamhfzql(x1"
export DB_HOST=rds-seedpay-dev.chmcrvnfoppe.us-east-1.rds.amazonaws.com
export DB_NAME=seedpaydb
export DB_USER=admseed
export DB_PASS=a5a4sd65f1a65
export DB_PORT=3306
export EPAYCO_PUBLIC_KEY=e45e28fb95e0375d361735837ed3f402
export EPAYCO_PRIVATE_KEY=00afefc81d6536b846710bd2f8d1213e