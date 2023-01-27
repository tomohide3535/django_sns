from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views import generic
from .forms import ProfileForm
from django.contrib.messages.views import SuccessMessageMixin

class ProfileEdit(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'edit.html'
    success_url = '/accounts/edit/'
    success_message = 'プロフィールを更新しました。'

    def get_object(self):
        return self.request.user


class OnlyUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.kwargs['pk'] == self.request.user.pk or self.request.user.is_superuser


class ProfileDetail(OnlyUserMixin, generic.DetailView):
    model = CustomUser
    template_name = 'detail.html'
    
    
edit = ProfileEdit.as_view()
detail = ProfileDetail.as_view()