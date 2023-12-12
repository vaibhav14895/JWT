
import email
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import student,userOtp
from .serializers import Studentserializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .utils import send_email_to_user
from django.contrib.auth.models import User
import uuid



class studentapi(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu=student.objects.get(id=pk)
            serializer=Studentserializer(stu)
            return Response(serializer.data)
        else:
            stu =student.objects.all()
            serializer=Studentserializer(stu,many=True)
            return Response(serializer.data)
        


    def post(self,request,pk=None,format=None):
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':serializer.data})
        else:
            return Response(serializer.errors)
        
    def put(self,request,pk=None,format=None):
        id=pk
        stu=student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'put complete'})
        else:
            return Response({'msg':'put is not done'})
        
    def patch(self,request,pk=None,format=None):
        id=pk
        stu=student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'put complete'})
        else:
            return Response({'msg':'put is not done'})
   
   
        
@api_view(['GET','POST'])      
def send_mail_to(request):
    if request.method=="POST":
        username=request.data.get("username")
        email=request.data.get("email")
        userdata = User.objects.filter(username=username,email=email).first()
        if userdata is not None:
            my_uuid = uuid.uuid4()
            parameter=str(my_uuid)
            otp_instance=userOtp(otp=parameter,username=username)
            otp_instance.save()
            send_email_to_user(email,parameter)
            return Response({"message": "Email sent successfully"})
        else:
            return Response({"message": "check username or email"})
    else:
        return Response({"msg":"something went wrong"})

    

        
@api_view(['GET','POST'])
def change_password(request, uid):
    if request.method=="POST":
        try:
            obj = userOtp.objects.get(otp=uid)
        except userOtp.DoesNotExist:
            return Response({"msg": "Invalid OTP"})

        try:
            user = User.objects.get(username=obj.username)
        except User.DoesNotExist:
            return Response({"msg": "User not found"})

        if user is not None:
            new_password = request.data.get("password")
            user.set_password(new_password)
            user.save()
            return Response({"msg": "Password changed successfully"})
        else:
            return Response({"msg": "Something went wrong"})
    return Response({"msg":"send password"})