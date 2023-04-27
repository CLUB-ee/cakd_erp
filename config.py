# config.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB NAME',
        'USER': 'DB USER NAME',  # mysql 유저 ID
        'PASSWORD': 'PASSWARD',  # mysql 유저 PW
        'HOST': '127.0.0.1',
        'PORT': '3306',  # mysql port
    }
}
