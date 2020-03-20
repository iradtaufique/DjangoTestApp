from django.urls import path

from singupApp.views import signup, home, CreatePersonal, PersonalListView, newUser, additioInformation

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='singupApp'),
    path('create/', CreatePersonal.as_view(), name='personal'),
    path('table/', PersonalListView.as_view(), name='table'),
    path('newUser/', newUser, name='newuser'),
    path('additionInfo/', additioInformation, name='additionInfo'),


]
