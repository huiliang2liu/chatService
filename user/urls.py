from django.conf.urls import url
import user_operation as u
import hxChat.upload_file as up


urlpatterns = [
        url("login", u.login),
        url("detail", u.detail),
        url("regist", u.regist),
        url("friends", u.friends),
        url("logout", u.logout),
        url("changePassword", u.changePassword),
        url("upload", up.upload),
    ]
def url():
    return urlpatterns,"user","user"
