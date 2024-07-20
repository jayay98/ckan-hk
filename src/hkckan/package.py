import requests
import json
from typing import List, Dict, Any

__all__ = [
	"list_packages", "show_package",
	"group_list", "group_show"
]
__BASE_URL = "https://data.gov.hk/tc-data/api/3/action" 

def list_packages(limit: int = 10, offset: int = 0) -> List[str]:
	payload = {
		"limit": limit, "offset": offset
	}
	url = __BASE_URL + "/package_list"

	response = requests.get(url, params=payload)
	response = response.json()

	if "success" not in response or response["success"] != True:
		raise Exception("Unsuccessful API request")

	if "result" not in response:
		raise Exception("No result")

	return response["result"]

def show_package(dataset_id: int) -> Dict[str, Any]:
	payload = {
		"id": dataset_id
	}
	url = __BASE_URL + "/package_show"
	response = requests.get(url, params=payload)
	response = response.json()

	if "success" not in response or response["success"] != True:
		raise Exception("Unsuccessful API request")

	if "result" not in response:
		raise Exception("No result")

	return response["result"]

def group_list() -> List[str]:
	url = __BASE_URL + "/group_list"
	response = requests.get(url)
	response = response.json()

	if "success" not in response or response["success"] != True:
		raise Exception("Unsuccessful API request")

	if "result" not in response:
		raise Exception("No result")

	return response["result"]

def group_show(group_id: int) -> Dict[str, Any]:
	payload = {
		"id": group_id
	}
	url = __BASE_URL + "/group_show"
	response = requests.get(url, params=payload)
	response = response.json()

	if "success" not in response or response["success"] != True:
		raise Exception("Unsuccessful API request")

	if "result" not in response:
		raise Exception("No result")

	return response["result"]