from django.contrib import admin

# Register your models here.
from .models import Level
from .models import Style
from .models import Genre
from .models import Song
from .models import Student
from .models import Purpose
from .models import Status
from .models import Update
from .models import Link
from .models import StudentSong


admin.site.register(Level)
admin.site.register(Style)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Student)
admin.site.register(Purpose)
admin.site.register(Status)
admin.site.register(Update)
admin.site.register(Link)
admin.site.register(StudentSong)
