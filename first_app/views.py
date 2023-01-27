from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

class IndexView(generic.TemplateView):
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        posts = Post.objects.order_by('-created_at')
        return posts

class CreateView(LoginRequiredMixin, generic.CreateView):
    #template_name = 'timeline.html'
    form_class = PostForm
    success_url = reverse_lazy('first_app:timeline')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました。')
        return super(CreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました。')
        return redirect('first_app:index')

index = IndexView.as_view()
create = CreateView.as_view()
