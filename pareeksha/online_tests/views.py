from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import OnlineTest
from .serializers import OnlineTestSerializer
from users.permissions import IsTeacher, IsTestOwner


class OnlineTestViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated ]
    serializer_class = OnlineTestSerializer

    def get_queryset(self):
        if self.request.user.is_student():
            return self.request.user.standard.online_tests.all()
        return OnlineTest.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
    def get_permissions(self):
        if self.action in ['update','partial_update','destroy']:
            self.permission_classes = [IsTestOwner,]
        elif self.action in ['create']:
            self.permission_classes = [IsTeacher,]
        else :
            self.permission_classes = [permissions.IsAuthenticated,]
        
        return [permission() for permission in self.permission_classes]
