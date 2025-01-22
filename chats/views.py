from django.views.generic import TemplateView


class ChatTemplateView(TemplateView):
    template_name = 'chats/chat.html'
