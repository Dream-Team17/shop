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

def discount_price_count(price, discount, discount_price):
    discount = discount
    price = price
    discount_price = discount_price
    if isinstance(discount, float or int) > 0 and discount_price == 0:
        discount_price_count = float(price) - ((float(discount) / 100) * float(price))
        return discount_price_count, discount
    elif discount == 0 and isinstance(discount_price, float or int) > 0:
        discount_count = float(price) - ((float(discount_price) * 100) / float(price))
        return discount_price, discount_count
    elif isinstance(discount, float or int) > 0 and isinstance(discount_price, float or int) > 0:
        discount_count = float(price) - ((float(discount_price) * 100) / float(price))
        return discount_price, discount_count

# def count_discount_percent(discount_percent, price, discount_price):
#     if isinstance(discount_percent, (float, int)) == 0 and isinstance(discount_price, (float, int)) > 0:
#         return f'{(100 - ((discount_price)* 100) / price)}'
#     elif isinstance(discount_percent, (float, int)) > 0 and isinstance(discount_price, (float, int)) > 0:
#         return f'{100 - ((discount_price * 100) / price)}'
#     elif isinstance(discount_percent, (float, int)) == 0 and isinstance(discount_price, (float, int)) == 0:
#         return f'{discount_percent}'
#     elif isinstance(discount_percent, (float, int)) > 0 and isinstance(discount_price, (float, int)) == 0:
#         return f'{discount_percent}'
#
#
# def count_discount_price(discount_percent, price, discount_price):
#     if isinstance(discount_percent, (float, int)) > 0 and isinstance(discount_price, (float, int)) == 0:
#         return f'{((100 - discount_percent) * price) / 100}'
#     elif isinstance(discount_percent, (float, int)) == 0 and isinstance(discount_price, (float, int)) > 0:
#         return f'{discount_price}'
#     elif isinstance(discount_percent, (float, int)) > 0 and isinstance(discount_price, (float, int)) > 0:
#         return f'{discount_price}'
#     elif isinstance(discount_percent, (float, int)) == 0 and isinstance(discount_price, (float, int)) == 0:
#         return f'{discount_price}'
