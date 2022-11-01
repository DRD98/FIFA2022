import json
from datetime import datetime
# from .models import Fixture
from django.http import JsonResponse
from rest_framework.views import APIView
# from fifa2022.settings import SECRET_KEY
# from rest_framework.permissions import IsAdminUser
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EventSerializer, TeamSerializer, TempSerializer#, FixtureSerializer, ViewFixtureSerializer, QuestionSerializer


# class createeventview(APIView):

#     # authenticaton_classes = ( JWTAuthentication, )
#     # permission_classes = ( IsAdminUser, IsAuthenticated, )

#     def post (self, request):
#         print(request.data)
#         serializer = EventSerializer(data = request.data)
#         if serializer.is_valid():
#         # serializer.is_valid()
#             # print ("\n\n", serializer.data, "\n\n")
#             serializer.save()
#             # print ("\n\n", serializer.data, "\n\n")
#             return JsonResponse ({"Status" : "Successful"})
#         # print ("\n\n", serializer.data, "\n\n")
#         return JsonResponse ({"Status" : "Unsuccessful"})
    
#     def patch (self, request):
#         print(request.data)
#         return JsonResponse ({"Status" : "Inside Patch"})


# class usereventview(APIView):

#     # authenticaton_classes = ( JWTAuthentication, )
#     # permission_classes = ( IsAdminUser, IsAuthenticated, )

#     def post (self, request):
#         print(request.data)
#         serializer = EventSerializer(data = request.data)
#         if serializer.is_valid():
#         # serializer.is_valid()
#             # print ("\n\n", serializer.data, "\n\n")
#             serializer.save()
#             # print ("\n\n", serializer.data, "\n\n")
#             return JsonResponse ({"Status" : "Successful"})
#         # print ("\n\n", serializer.data, "\n\n")
#         return JsonResponse ({"Status" : "Unsuccessful"})

class createteamview(APIView):

    # authenticaton_classes = ( JWTAuthentication, )
    # permission_classes = ( IsAdminUser, IsAuthenticated, )

    def post (self, request):
        print(request.data)
        serializer = TeamSerializer(data = request.data)
        if serializer.is_valid():
        # serializer.is_valid()
            # print ("\n\n", serializer.data, "\n\n")
            serializer.save()
            # print ("\n\n", serializer.data, "\n\n")
            return JsonResponse ({"Status" : "Successful"})
        # print ("\n\n", serializer.data, "\n\n")
        return JsonResponse ({"Status" : "Unsuccessful"})


class createtempview(APIView):

    def post (self, request):
        print(request.data)
        serializer = TempSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse ({"Status" : "Successful"})
        return JsonResponse ({"Status" : "Unsuccessful"})


# class createfixtureview(APIView):

#     # authenticaton_classes = ( JWTAuthentication, )
#     # permission_classes = ( IsAdminUser, IsAuthenticated, )

#     def post (self, request):
#         # jsonfile = open('fifa22_app\DataFile\data.json', 'r')
#         # jsondata = jsonfile.read()
#         # print ("\n\n JsonData - ", jsondata, "\n\n")
#         # print(request.data)
#         respond = json.loads(request.body.decode('utf-8'))
#         print ("\n\n Respond - ", respond, "\n\n")
#         # serializer = FixtureSerializer(data=request.data)
#         serializer = FixtureSerializer(data = respond, many = False)
#         print ("\n\n Respond['start_time'] - ", respond['start_time'], "\n\n")
#         time = respond['start_time']
#         print ("\n\n Type - ", type( respond['start_time']), "\n\n")
#         format_data = "%Y-%m-%d %H:%M:%S.%f"
#         respond['start_time'] = datetime.strptime(time, format_data)
#         print ("\n\n Type - ", type( respond['start_time']), "\n\n")
#         if serializer.is_valid():
#         # serializer.is_valid()
#             print ("\n\n serializer.errors - ", serializer.errors, "\n\n")
#             # print ("\n\n Seriallizer Data - ", serializer.data, "\n\n")
#             serializer.save()
#             print ("\n\n", serializer.data, "\n\n")
#             return JsonResponse ({"Status" : "Successful"})
#         # print ("\n\n", serializer.data, "\n\n")
#         print ("\n\n serializer.errors - ", serializer.errors, "\n\n")
#         return JsonResponse ({"Status" : "Unsuccessful"})


# class userfixtureview(APIView):
    
#     # authenticaton_classes = ( JWTAuthentication, )  #user.is_staff has to be true
#     # permission_classes = ( IsAuthenticated, )

#     def get (self, request):
#         respond = request.POST
#         response = respond.dict()
#         # print ("\n\n response - ", response, "\n\n")
#         # event_id = 
#         if (response['event_id'] == '1'):
#             student = Fixture.objects.all()
#             serializer = ViewFixtureSerializer(student, many = True)
#             return JsonResponse ({"Status" : "Successful", "Data ": serializer.data})
#         # serializer.valid()
#         return JsonResponse ({"Status" : "Unsuccessful"})


# class createquestionview(APIView):

#     # authenticaton_classes = ( JWTAuthentication, )
#     # permission_classes = ( IsAdminUser, IsAuthenticated, )

#     def post (self, request):
#         print(request.data)
#         serializer = QuestionSerializer(data = request.data)
#         print ("\n\n Outside is_valid() \n\n")
#         if serializer.is_valid():
#         # serializer.is_valid()
#             print ("\n\n Inside is_valid() \n\n")
#             serializer.save()
#             # print ("\n\n", serializer.data, "\n\n")
#             return JsonResponse ({"Status" : "Successful"})
#         # print ("\n\n", serializer.data, "\n\n")
#         return JsonResponse ({"Status" : "Unsuccessful"})
