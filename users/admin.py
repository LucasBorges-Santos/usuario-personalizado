from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm


# formularios admin padrão
# admin.site.register(User, auth_admin.UserAdmin)

# formularios admin personalizados
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    # adicionando campos personalizado (bio)
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campo Personalizado", {"fields": ("bio",)}),
    )
