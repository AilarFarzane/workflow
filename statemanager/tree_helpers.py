import os.path

import pydotplus
from graphviz import Source
from django.db.models import Prefetch

def generate_user_action_graph(user_id):
    from statemanager.models import ActionStatePath


    # Get all ActionStatePath objects for the given user
    user_paths = (
        ActionStatePath.objects.filter(user_id=user_id)
        .select_related('action__starting_state', 'action__ending_state')
    )

    # Initialize a directed graph
    graph = pydotplus.Dot(graph_type='digraph', rankdir='LR')

    # Create nodes and edges
    for path in user_paths:
        action = path.action
        starting_state = action.starting_state.name
        ending_state = action.ending_state.name

        # Add nodes for states
        graph.add_node(pydotplus.Node(starting_state, shape="circle"))
        graph.add_node(pydotplus.Node(ending_state, shape="circle"))

        # Add an edge for the action
        graph.add_edge(pydotplus.Edge(
            starting_state,
            ending_state,
            label=action.name,
            color=action.color,
        ))

    # Output the graph as a PNG file
    folder_path = os.path.abspath("graphs")
    output_path = os.path.join(folder_path, f"user_{user_id}_action_graph.png")
    graph.write_png(output_path)

    print(f"Graph saved to {output_path}")
    return output_path


