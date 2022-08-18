from rest_framework import generics
from .models import UserAccount
from .serializers import UserCreateSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    authentication_classes = [] 
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class RetrieveUserView(generics.ListAPIView):
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return UserAccount.objects.all()
    