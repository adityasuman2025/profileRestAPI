from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import permissions
from . import serializers
from . import models

# Create your views here.

class HelloApiView( APIView ):
	"""Testing API View"""

	serializer_class = serializers.HelloSerializer

	def get( self, request, format = None ):
		"""Returns a list of APIView features"""

		an_apiview = [
			'Uses HTTP methods as function i.e ( get, post, patch, put, delete )',
			'It is similar to a traditional Django view',
			'Gives me the most control of my logic',
			'Is mapped manually to URLs'
		]

		return Response( { 'message': "Hello bro!", 'an_api_view': an_apiview } )

	def post( self, request ):
		"""create a hello messgae with our name"""

		serializer = serializers.HelloSerializer( data = request.data )

		if serializer.is_valid():
			name = serializer.data.get( "name" )
			message = "Hello " + name

			return Response( { 'message': message } )
		else:
			return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

	def put( self, request, pk = None ):
		"""handles updating an object"""

		return Response( { 'method': 'put run ', 'message': request.data } )

	def patch( self, request, pk = None ):
		"""handles updating only fields provided in the rqst"""

		return Response( { 'method': 'patch run ', 'message': request.data } )

	def delete( self, request, pk = None ):
		"""handles deleting an object"""

		return Response( { 'method': 'delete run ', 'message': request.data } )


class HelloViewSet( viewsets.ViewSet ):
	"""Testing View Sets"""

	serializer_class = serializers.HelloSerializer # verify/test user's input

	def list( self, request ):
		"""Returns a hello message"""

		a_viewset = [
			"Uses actions (list, create, retrive, update, partial_update, destroy)",
			"Automatically maps to URLs using Routers",
			"Provides more functionality with less code",
		]

		return Response( { 'message': "Hello!", 'a_viewset': a_viewset } )

	def create( self, request ):
		"""create a new hello messgae with our name"""

		serializer = serializers.HelloSerializer( data = request.data )

		if serializer.is_valid():
			name = serializer.data.get( "name" )
			message = "Hello " + name

			return Response( { 'message': message } )
		else:
			return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

	def retrieve( self, request, pk = None ):
		"""handles getting an object by its ID"""

		return Response( { 'http_method': 'GET' } )

	def update( self, request, pk = None ):
		"""handles updating an object"""

		return Response( { 'http_method': 'put' } )

	def partial_update( self, request, pk = None ):
		"""handles updating only fields provided in the rqst"""

		return Response( { 'http_method': 'patch' } )

	def destroy( self, request, pk = None ):
		"""handles deleting an object"""

		return Response( { 'http_method': 'delete' } )


class UserProfileViewSet( viewsets.ModelViewSet ):
	"""Handles creating and updating profiles"""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all() # to display/list output from a model/database on GET rqst

	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( permissions.UpdateOwnProfile, )
	filter_backends = ( filters.SearchFilter, )
	search_fields = ( "name", "email", )


class LoginViewSet( viewsets.ViewSet ):
	"""checks email and password and returns auth token"""

	serializer_class = AuthTokenSerializer

	def create( self, request ):
		"""use the ObtainAuthToken APIView to validate and create a token"""

		return ObtainAuthToken().post( request )


class UserProfileFeedViewSet( viewsets.ModelViewSet ):
	"""Handles creating, reading and updating profile feed items"""

	authentication_classes = ( TokenAuthentication, )
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all() # to display/list output from a model/database on GET rqst
	permission_classes = ( permissions.PostOwnFeed, IsAuthenticated )

	def perform_create( self, serializer ):
		"""sets the user_profile column value of the Profilefeed model as the logged in user"""

		serializer.save( user_profile = self.request.user )
