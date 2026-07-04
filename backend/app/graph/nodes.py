from app.agents.intent_agent import IntentAgent
from app.agents.crawl_config_agent import CrawlConfigAgent
from app.agents.extraction_agent import ExtractionAgent

from app.crawler.runner import run_crawler

intent_agent = IntentAgent()
config_agent = CrawlConfigAgent()
extract_agent = ExtractionAgent()


def intent_node(state):

    if state["mode"] == "urls":
        return state

    result = intent_agent.run(state["intent"])

    state["urls"] = result["suggested_urls"]

    return state


def config_node(state):

    state["crawl_config"] = config_agent.run(state["urls"])

    return state


def crawl_node(state):

    state["raw_data"] = run_crawler(state["urls"])

    return state


def extraction_node(state):

    result = extract_agent.run(
        state["raw_data"],
        state["intent"]
    )

    state["processed_data"] = result["results"]

    return state


def export_node(state):

    return state