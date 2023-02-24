import os
from datetime import datetime
now = datetime.now()


def path_and_rename(instance, filename):
    now = datetime.now()
    upload_to = 'product_images'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = f'{now.strftime("%d-%m-%Y %H-%M")}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


def path_and_rename2(instance, filename):
    upload_to = 'category_images'
    ext = filename.split('.')[-1]

    filename = f'{now.strftime("%d-%m-%Y %H-%M")}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


def path_and_rename3(instance, filename):
    upload_to = 'subcategory_images'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = f'{now.strftime("%d-%m-%Y %H-%M")}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)
