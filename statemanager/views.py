from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404
from django.views.decorators.http import require_POST

from .models import Action, ActionStatePath
from .tree_helpers import  generate_user_action_graph

User = get_user_model()
import os



def UserList(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {"users":users})



def UserApplyAction(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    current_state = user.current_state
    actions = Action.objects.filter(starting_state=current_state)

    if request.method == "POST":
        action_id = request.POST.get('action')

        # print(action_id)
        if action_id:
            action = get_object_or_404(Action, pk=action_id)
            user.current_state = action.ending_state

            user_path = ActionStatePath.objects.create(
                user=user,

                action=action,
                )
            print(user_path)

            user.save()

            return redirect('user-actions', user_id=user_id)

    return render(request, 'user_actions.html', context={
        'actions':actions,
        'user':user,
        'current_state':current_state
    })




def user_action_tree_view(request, user_id):
    try:
        # Generate the graph and get the path
        graph_path = generate_user_action_graph(user_id)

        # Check if the file exists before returning it
        if os.path.exists(graph_path):
            # Return the file as a response
            return FileResponse(open(graph_path, 'rb'), content_type='image/png')
    except:
            raise FileNotFoundError("Graph file was not created")
    # except FileNotFoundError:
    #     return render(request, 'login.html', {'message': 'Graph not found'})
    # except Exception as e:
    #     # Catch any unexpected exceptions
    #     return render(request, 'login.html', {'message': f'Error: {str(e)}'})



