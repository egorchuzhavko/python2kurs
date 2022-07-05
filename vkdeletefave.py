from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id

vk_session = VkApi('+375445153004', 'dudlikqaz123')
vk_session.auth(token_only=True)

vk = vk_session.get_api()

vk.messages.send(user_id=0, message='Сообщение', random_id=get_random_id())