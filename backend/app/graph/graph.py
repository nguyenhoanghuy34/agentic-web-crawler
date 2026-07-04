from langgraph.graph import StateGraph

from app.graph.state import GraphState

from app.graph.nodes import (
    intent_node,
    config_node,
    crawl_node,
    extraction_node,
    export_node
)

builder = StateGraph(GraphState)

builder.add_node("intent", intent_node)
builder.add_node("config", config_node)
builder.add_node("crawl", crawl_node)
builder.add_node("extract", extraction_node)
builder.add_node("export", export_node)

builder.set_entry_point("intent")

builder.add_edge("intent", "config")
builder.add_edge("config", "crawl")
builder.add_edge("crawl", "extract")
builder.add_edge("extract", "export")

builder.set_finish_point("export")

graph = builder.compile()