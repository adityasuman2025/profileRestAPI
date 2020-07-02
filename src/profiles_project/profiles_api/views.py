from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView( APIView ):
	"""Test API View"""

	def get( self, request, format = None ):
		"""Returns a list of APIView features"""

		an_apiview = [
			'Uses HTTP methods as function i.e ( get, post, patch, put, delete )',
			'It is similar to a traditional Django view',
			'Gives me the most control of my logic',
			'Is mapped manually to URLs'
		]

		return Response( { 'message': "Hello bro!", 'an_api_view': an_apiview } )