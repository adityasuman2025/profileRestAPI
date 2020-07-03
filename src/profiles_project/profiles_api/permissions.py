from rest_framework import permissions

class UpdateOwnProfile( permissions.BasePermission ):
	"""Allow users to edit their own profile"""

	def has_object_permission( self, request, view, obj ):
		"""check if user is trying to edit their own profile"""

		if request.method in permissions.SAFE_METHODS: # if method is safe i.e GET then no need of any validation // user can view other user's profile
			return True

		return obj.id == request.user.id


class PostOwnFeed( permissions.BasePermission ):
	"""Allow users to update their own feed"""

	def has_object_permission( self, request, view, obj ):
		"""check if user is trying to add his own feed only"""

		if request.method in permissions.SAFE_METHODS: # if method is safe i.e GET then no need of any validation // user can view other user's feed
			return True

		return obj.user_profile.id == request.user.id