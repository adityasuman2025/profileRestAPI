from rest_framework import serializers

from . import models

class HelloSerializer( serializers.Serializer ):
	"""Serializes a name field for tesing our APIView"""

	name = serializers.CharField( max_length = 10 )


class UserProfileSerializer( serializers.ModelSerializer ):
	"""A serializer for our user profile objects"""

	class Meta:
		model = models.UserProfile
		fields = ( 'id', 'name', 'email', 'password' ) #tuple
		extra_kwargs = { 'password': { 'write_only': True } }

	def create( self, validated_data ):
		"""creates and returns a new user."""

		user = models.UserProfile(
			email = validated_data["email"],
			name = validated_data["name"],
		)


		user.set_password( validated_data['password'] )
		user.save()

		return user


class ProfileFeedItemSerializer( serializers.ModelSerializer ):
	"""A serializer for profile feed items"""

	class Meta:
		model = models.ProfileFeedItem
		fields = ( 'id', 'user_profile', 'feed_text', 'created_on' ) #tuple
		extra_kwargs = { 'user_profile': { 'read_only': True } }

