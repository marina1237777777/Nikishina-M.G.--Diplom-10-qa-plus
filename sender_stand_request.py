import configuration
import requests
import data


#Создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers).json()["track"]


# Сохранение номера трека заказа
def get_new_order_track(track_number):
    params = {"t": track_number}
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                         params =params,
                         headers=data.headers)
    return response
