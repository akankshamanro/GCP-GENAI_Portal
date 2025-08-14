import pytest
from app import views

def test_submit_complaint():
    # Test case 1: complaint text is empty
    response = views.submit_complaint()
    assert response.status_code == 200
    assert response.json == {"error": "Complaint text is empty"}

    # Test case 2: complaint text is not empty
    data = {"complaintText": "This is a test complaint."}
    response = views.submit_complaint(json=data)
    assert response.status_code == 200
    assert "generated_text" in response.json