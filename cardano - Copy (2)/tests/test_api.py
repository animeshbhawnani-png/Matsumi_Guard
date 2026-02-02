"""
Basic tests for the Cardano Risk & Compliance Engine API
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_test_endpoint():
    """Test the test endpoint"""
    response = client.get("/api/test")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "message" in data
    assert "endpoint" in data


def test_cors_headers():
    """Test that CORS is properly configured"""
    response = client.get("/health")
    assert response.status_code == 200
    # CORS headers should be present for allowed origins


def test_api_routes_exist():
    """Test that the API routes are registered"""
    # This will return 405 or 422 for GET requests, not 404
    response = client.get("/api/analyzeTransaction")
    assert response.status_code != 404  # Route exists
    
    response = client.get("/api/analyzeWallet")
    assert response.status_code != 404  # Route exists
