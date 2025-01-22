from django.urls import path

from .views import (
    ChatTemplateView,
)


urlpatterns = [
    path('', ChatTemplateView.as_view(), name="chat-template"),

]
