from django.contrib import admin
from .models import state, action, ActionStatePath


class stateAdmin(admin.ModelAdmin):
    model = state

    list_display = ['name', 'description' , 'color']


class actionAdmin(admin.ModelAdmin):
    model = action
    list_display = ['name', 'starting_state', 'ending_state', 'description', 'color']


class ActionStatePathAdmin(admin.ModelAdmin):
    model = ActionStatePath
    fields = ['user', 'action']
    readonly_fields = ['current_state']
    list_display = ['user', 'current_state']






admin.site.register(state, stateAdmin)
admin.site.register(action, actionAdmin)
admin.site.register(ActionStatePath, ActionStatePathAdmin)
