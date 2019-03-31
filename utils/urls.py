from django.conf.urls import url
import city



urlpatterns = [
        url("city", city.parse),
        url("cardCity", city.card_city),
        url("cardSex", city.card_sex),
        url("cardBirthday", city.card_birthday),
    ]
def url():
    return urlpatterns,"utils","utils"
