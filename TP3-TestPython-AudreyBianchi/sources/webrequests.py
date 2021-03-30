from sources import webrequests
import pytest

def test_doGet():
    # Arrange
    URL = "http://www.facebook.com"
    
    # Act
    with pytest.raises(LookupError):
        data = webrequests.doGet(URL)

    # Assert
    assert data is not None
    #assert data == b"<Html><Head><Title>Vous Etes Perdu ?</Title></Head><Body><H1>Perdu Sur L'Internet ?</H1><H2>Pas De Panique, On Va Vous Aider</H2><Strong><Pre>    * <----- Vous &Ecirc;Tes Ici</Pre></Strong></Body></Html>\n"