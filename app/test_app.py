from app import app

def test_homepage():
	tester = app.test_client()
	response = tester.get('/')
	assert response.status_code == 200
	assert "Mesaj Gönder" in response.data.decode("utf-8")
