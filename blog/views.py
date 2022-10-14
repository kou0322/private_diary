import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import BlogInquiryForm

logger = logging.getLogger(__name__)


class BlogIndexView(generic.TemplateView):
    template_name = "blogindex.html"

class BlogInquiryView(generic.FormView):
    template_name = "bloginquiry.html"
    form_class = BlogInquiryForm
    success_url = reverse_lazy('blog:bloginquiry')

    def form_valid(self, form):
        form.send_title()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('BlogInquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
