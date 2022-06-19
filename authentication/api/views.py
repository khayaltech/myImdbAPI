from os import stat
from urllib import response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
def registirationView(request):
  if request.method=='POST':
    serializer=RegistrationSerializer(data=request.data)
    data={}
    if serializer.is_valid():
      account=serializer.save()
      data['message']='Your profile is ready 👦'
      data['username']=account.username
      data['email']=account.email
      
      #For token Authentication
      data['token']=Token.objects.get(user=account).key
      
      #For JWT authentication
      # refresh = RefreshToken.for_user(account)
      # data['token']={
      #   'refresh': str(refresh),
      #   'access': str(refresh.access_token),
      #   }
        
    else:
       data=serializer.errors
    
    return Response(data,status.HTTP_201_CREATED)


@api_view(['POST'])
def logoutView(request):
  if  request.method=='POST':
    print(request.user)
    request.user.auth_token.delete()
    return Response({'message':'You are logged out succesfully'},status=status.HTTP_200_OK)
  
    
  