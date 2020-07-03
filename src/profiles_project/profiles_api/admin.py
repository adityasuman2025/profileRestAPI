from django.contrib import admin

from . import models  # . means current location ( the same directory )

# Register your models here.

admin.site.register( models.UserProfile )
admin.site.register( models.ProfileFeedItem )