from django.urls import path
from .views import PerfectINFO
app_name = 'organizer'
urlpatterns = [
    path('perfect-info', view=PerfectINFO)
]