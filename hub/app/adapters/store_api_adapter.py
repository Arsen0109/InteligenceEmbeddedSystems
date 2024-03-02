import json
from typing import List

import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        json_data = [json.loads(agent_data.json) for agent_data in processed_agent_data_batch]
        response: requests.Response = requests.post(self.api_base_url + "/processed_agent_data/", json=json_data)
        return response.status_code == 200
