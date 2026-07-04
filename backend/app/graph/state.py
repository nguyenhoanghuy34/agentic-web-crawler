from typing import TypedDict, Any


class GraphState(TypedDict):

    job_id: str

    mode: str

    intent: str

    urls: list[str]

    crawl_config: dict[str, Any]

    raw_data: list

    processed_data: list

    export_file: str