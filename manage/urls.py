from django.conf.urls import url
import user_mamage as manage
urls=[url("all",manage.all_user),
      url("delete",manage.delete_user),
      url("clear",manage.delete_all_user),
      ]
def url():
    return urls,"manage","manage"