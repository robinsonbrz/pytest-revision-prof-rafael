from unittest.mock import patch
from mock.fetch_www import parse

@patch('mock.fetch_www.fetch_net')
def test_parse_from_fetch_net(mock_get):
    mock_get.return_value = "def"
    assert parse() == "def123"


import pytest
from unittest.mock import patch
from fetch_www import fetch_net

@patch('fetch_www.requests.get')
def test_fetch_net_success(mock_get):
    # Arrange
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    
    # Act
    result = fetch_net()
    
    # Assert
    assert result == "abc"
    mock_get.assert_called_once()

@patch('fetch_www.requests.get')
def test_fetch_net_failure(mock_get):
    # Arrange
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    
    # Act
    result = fetch_net()
    
    # Assert
    assert result == "bcd"
    mock_get.assert_called_once()
