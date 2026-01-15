import pytest
import requests
def make_request_with_id(id):
    base_url = "http://127.0.0.1:2500/items/"
    response = requests.get(f'{base_url}{id}')
    return response
def test_search_item_with_success():
    # Arrange:
    
    #Act:
    response = make_request_with_id(12)
    #Assertion:
    assert response.status_code == 200  # Validation of status code  
    data = response.json()  
    # Assertion of body response content:  
    assert len(data) > 0  
    assert data["item_id"] == 12