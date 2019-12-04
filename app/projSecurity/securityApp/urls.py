from django.urls import include, path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('results/', views.results, name='results'),
#     path('gtts/', include('gTTS.urls')),
#     path('gtts_auth/', include('gTTS.urls_auth')),
#
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.index, name='results'),
    path('results/', views.playSound, name='playSound'), #  <form action="{% url 'playSound' %} >"
    path('gtts/', include('gTTS.urls')),
    path('gtts_auth/', include('gTTS.urls_auth')),
]
