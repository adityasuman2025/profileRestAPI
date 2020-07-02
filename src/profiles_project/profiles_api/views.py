from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.


class HelloApiView( APIView ):
	"""Test API View"""

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

