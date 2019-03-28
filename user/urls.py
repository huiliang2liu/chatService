from django.conf.urls import url
import user_operation as u


urlpatterns = [
        url("login", u.login),
        url("detail", u.detail),
        url("regist", u.regist),
        url("friends", u.friends),
        url("logout", u.logout),
        url("changePassword", u.changePassword),
    ]
def url():
    return urlpatterns,"user","user"
