from django.contrib import admin
from .models import Company
from .models import Category
from .models import Nationality
from .models import Status
from .models import LowSkill
from .models import Case

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Nationality)
admin.site.register(Status)
admin.site.register(LowSkill)
admin.site.register(Case)
