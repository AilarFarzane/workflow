from django.contrib import admin
from .models import State, Action, ActionStatePath


class stateAdmin(admin.ModelAdmin):
    model = State

    list_display = ['name', 'description' , 'color']


class actionAdmin(admin.ModelAdmin):
    model = Action
    list_display = ['id','name', 'starting_state', 'ending_state', 'description', 'color']


class ActionStatePathAdmin(admin.ModelAdmin):
    model = ActionStatePath
    fields = ['user', 'action']
    readonly_fields = ['current_state']
    list_display = ['user', 'current_state']






admin.site.register(State, stateAdmin)
admin.site.register(Action, actionAdmin)
admin.site.register(ActionStatePath, ActionStatePathAdmin)
