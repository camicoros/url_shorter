from django.urls import path, re_path

from .views import RedirectListView, RedirectCreateView, RedirectCounterView, RedirectDetailView

app_name = 'url_shorter_app'
urlpatterns = [
    path('', RedirectCreateView.as_view(), name='create'),
    path('list/', RedirectListView.as_view(), name='index'),
    re_path(r'(?P<short_path>[A-Za-z0-9]{6})/detail/', RedirectDetailView.as_view(), name='detail'),
    re_path(r'(?P<short_path>[A-Za-z0-9]{6})/', RedirectCounterView.as_view(), name='redirect'),

]
