from django.contrib import admin
from .models import Female , Male , Items , User , Video , UserVideo , Login
# Register your models here.
#admin.site.register(Female)
#admin.site.register(Male)
#admin.site.register(Items)
#admin.site.register(User)
#admin.site.register(Video)
#admin.site.register(UserVideo)
admin.site.register(Login)
admin.site.site_header = 'practice website '
admin.site.site_title = 'Oraby'