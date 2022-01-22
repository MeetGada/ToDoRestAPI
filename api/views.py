from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import work
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Using generic views to enchance the performace
class userRegister(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# this class will be used to create tasks
class addWork(ListCreateAPIView):
    queryset = work.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = workSerializer 
    
    def perform_create(self, serializer):
        # saving user/owner of the task
        serializer.save(user=self.request.user)

# this class will return all the tasks of the user
class taskList(APIView):
    # here, using APIView to filter the tasks based on the user requesting data
    serializer_class = workSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return work.objects.all()
    
    def get(self, request, *args, **kwargs):
        tasks = work.objects.filter(user=request.user.id)
        serializer = workSerializer(tasks, many=True)
        return Response(serializer.data)

# this class will be used to update/delete the tasks
class edit_task(RetrieveUpdateDestroyAPIView):
    queryset = work.objects.all()
    # IsOwner is the custom permission class created to verify the owner of the task
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = workSerializer

class logoutUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
    # deleting the auth token to avoid it's reuse after logging out
        user.auth_token.delete()
        return Response({'msg':'Logged out successfully!'})

    
