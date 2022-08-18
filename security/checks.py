from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse

class IsAdminCheck(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Sysadmin').exists()
    def handle_no_permission(self):
        return HttpResponse("Your request was forbidden")