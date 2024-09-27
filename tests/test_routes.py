import io
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def valid_pdf_file():
    return io.BytesIO(b"%PDF-1.5 ... some PDF content ...")


@pytest.fixture
def invalid_file():
    return io.BytesIO(b"This is not a valid PDF or PPTX file")


def test_validate_slide_deck(valid_pdf_file, invalid_file):
    # Test with a valid PDF file
    response = client.post(
        "/slides/validate",
        files={"file": ("test.pdf", valid_pdf_file, "application/pdf")})
    assert response.status_code == 200
    result = response.json()
    assert "results" in result
    assert "all_passed" in result
    assert isinstance(result["results"], dict)
    assert isinstance(result["all_passed"], bool)

    # Test with an invalid file
    response = client.post(
        "/slides/validate",
        files={"file": ("test.txt", invalid_file, "text/plain")})
    assert response.status_code == 400
    assert "error" in response.json()

    # Test with no file
    response = client.post("/slides/validate")
    assert response.status_code == 422  # Unprocessable Entity

    # Test with URL instead of file
    response = client.post("/slides/validate",
                           data={"url": "http://example.com/slides.pdf"})
    assert response.status_code == 200
    result = response.json()
    assert "results" in result
    assert "all_passed" in result

    # Test with invalid URL
    response = client.post("/slides/validate", data={"url": "not_a_valid_url"})
    assert response.status_code == 400
    assert "error" in response.json()

    # Test with both file and URL (should prioritize file)
    response = client.post(
        "/slides/validate",
        files={"file": ("test.pdf", valid_pdf_file, "application/pdf")},
        data={"url": "http://example.com/slides.pdf"})
    assert response.status_code == 200
    result = response.json()
    assert "results" in result
    assert "all_passed" in result


def test_submit_slide_deck():
    # This test needs to be expanded once the endpoint is fully implemented
    response = client.post("/slides/submit",
                           json={
                               "content": "dGVzdA==",
                               "filename": "test.pdf",
                               "file_format": "PDF"
                           })
    assert response.status_code == 200
    assert response.json() == {"message": "Slide deck submitted successfully"}


def test_admin_root():
    # This test will fail until we implement proper authentication
    response = client.get("/admin/")
    assert response.status_code == 401  # Expecting unauthorized error


def test_admin_stats():
    # This test will fail until we implement proper authentication
    response = client.get("/admin/stats")
    assert response.status_code == 401  # Expecting unauthorized error


def test_admin_configure():
    # This test will fail until we implement proper authentication
    response = client.post("/admin/configure")
    assert response.status_code == 401  # Expecting unauthorized error
