import vk_api
import sys
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
if __name__ == '__main__':
    weather = get_weather()
text = event.obj["message"]["text"].split()
def write_message(sender,message):
	authorize.method('messages.send',{'user_id':sender,'message':message, "random_id": get_random_id()})
token = "e23d38ffe491fe3244288e7ef0a766609e6258c69705c07bca5e022f2eece73809486d30945ca7e71b200"
authorize = vk_api.VkApi(token = token)
longpoll=VkLongPoll(authorize)
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
		reseived_message=event.text
		sender=event.user_id
		if reseived_message=="Привет":
			write_message(sender,"Вассап")
		elif reseived_message=="Пока":
			write_message(sender,"бб")
		elif reseived_message=="нет":
			write_message(sender,"ноуп")
		elif reseived_message=="да":
			write_message(sender,"ага")
		elif reseived_message=="погода":
			write_message(sender,f'Погода сейчас {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}')
	if (len(text)>=2) and (text[0]=="Погода"):
		def get_weather():
			url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
			city = text[1]
			params = { 'key': '144918d90e3b4b2996b150427202810',
            	'q': city,
            	'format': 'json',
            	'num_of_days': 1,
            	'lang': 'ru'}
			r = requests.get(url, params=params)
			the_weather = r.json()
			if 'data' in the_weather:
					if 'current_condition' in the_weather['data']:
					try:
						return the_weather['data']['current_condition'][0]
					except(IndexError, TypeError):
						return 'Server Error'
			return 'Server Error'
			weather = get_weather()
			write_message(sender,f'Погода сейчас {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}')
