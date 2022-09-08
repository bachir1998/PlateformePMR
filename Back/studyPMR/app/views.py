from syslog import closelog
from rest_framework import viewsets
from .serializers import *
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from .utils import get_tokens_for_user
from django.shortcuts import get_object_or_404

# Create your views here.


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            current_user = get_object_or_404(MyUser.objects.filter(email = request.data["email"]))
            #TODO : create new pmr or bailleur
            role_user = current_user.role
            if role_user == 'pmr':
                serializer_pmr = PmrSerializer(data={'user_id':current_user.id})
                if serializer_pmr.is_valid():
                    serializer_pmr.save()

            if role_user == 'bailleur':
                serializer_bailleur = BailleurSerializer(data={'user_id':current_user.id})
                if serializer_bailleur.is_valid():
                    serializer_bailleur.save()

            return Response({'msg': 'Registration Success','id' : current_user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)

            pmr = Pmr.objects.filter(user_id = user.id)
            bailleur = Bailleur.objects.filter(user_id = user.id)
            

            if pmr:
                serializer = PmrSerializer(pmr, many=True)
            

            if  bailleur:
                serializer = BailleurSerializer(bailleur, many=True)
            

            return Response({'msg': 'Login Success','user_data' : serializer.data, **auth_data}, status=status.HTTP_200_OK)
        
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


      
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True) #Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BailleurViewSet(viewsets.ModelViewSet):
    queryset = Bailleur.objects.all()
    serializer_class = BailleurSerializer
    permission_classes = (IsAuthenticated,)

class PmrViewSet(viewsets.ModelViewSet):
    queryset = Pmr.objects.all()
    serializer_class = PmrSerializer
    permission_classes = (IsAuthenticated,)


class LogementViewSet(viewsets.ModelViewSet):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer
    permission_classes = (IsAuthenticated,)


class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = (IsAuthenticated,)
