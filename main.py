from graph.pipeline import build_graph

graph = build_graph()
state = {}
final_state = graph.invoke(state)

print(final_state.keys())

