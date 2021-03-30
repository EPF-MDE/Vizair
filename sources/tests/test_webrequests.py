import pytest
import requests
from sources import webrequests

def test_doGet():
    #Arrange
    URL = "https://notepad-plus-plus.org/"

    #Act
    act = webrequests.doGet(URL)

    #Assert
    assert act is not None

def test_doGetUnknown():
    #Arrange
    URL = "https://notepad-plus-plus.org/"

    #Act
    with pytest.raises(requests.exceptions.ConnectionError):
        act = webrequests.doGet(URL)
    

    #Assert
    # assert act is not None
    
    


