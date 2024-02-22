docker-compose build

DB の編集ファイルをいじってから
 docker-compose up -d

 コンテナに入って、django-admin.py startproject django_app を打ち込む



settings.py の変更  ALLOWED_HOSTS = ['*']


python manage.py runserver 0.0.0.0:8000  コマンドを実行
