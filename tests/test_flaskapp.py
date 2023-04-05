from flaskapp.models import User


def test_index(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/'
    THEN the status code should be 302, this is due to a browser is open and open a link "/""
    """
    response = test_client.get("/")
    assert response.status_code == 302
    
    
def test_home(test_client):
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data
    
    
def test_registration(test_client, app):
    response = test_client.post("/sign-up", data={"email": "test@test.com", "firstName": "testfirstname", "password1": "114302ab", "password2": "114302ab"})

    with app.app_context():
        assert User.query.offset(1).first().email == "test@test.com"
        
        
def test_whether_login_successfully(test_client):
    test_client.post("/sign-up", data={"email": "test@test.com", "firstName": "testfirstname", "password1": "114302ab", "password2": "114302ab"})
    test_client.post("/login", data={"email": "test@test.com", "password": "114302ab"})

    response = test_client.get("/")
    responses = test_client.post("/", data={"note": "testnote"})
    assert b"Home" in response.data
    assert b"Please leave any of your advice and report mistake here" in response.data
    assert b"Note added!" in responses.data

def test_Education_expenditure_page(test_client):
    test_client.post("/sign-up", data={"email": "test@test.com", "firstName": "testfirstname", "password1": "114302ab", "password2": "114302ab"})
    test_client.post("/login", data={"email": "test@test.com", "password": "114302ab"})

    response = test_client.get("/Education_expenditure")
    responses = test_client.post("/Education_expenditure", data={"Years": "1833"})

    assert b"UK public expenditure on education" in response.data
    assert b"Current_prices in thousands: 57.5" in responses.data
    assert b"Data found!" in responses.data
    
def test_Education_enrolment_page(test_client):
    test_client.post("/sign-up", data={"email": "test@test.com", "firstName": "testfirstname", "password1": "114302ab", "password2": "114302ab"})
    test_client.post("/login", data={"email": "test@test.com", "password": "114302ab"})

    response = test_client.get("/Education_enrolment")
    responses = test_client.post("/Education_enrolment", data={"Years": "1854"})

    assert b"UK number of enrolment data search" in response.data
    assert b"TOTAL number of enrolment people: 461445.0" in responses.data
    assert b"Data found!" in responses.data
    
def test_Institute_distribution_page(test_client):
    test_client.post("/sign-up", data={"email": "test@test.com", "firstName": "testfirstname", "password1": "114302ab", "password2": "114302ab"})
    test_client.post("/login", data={"email": "test@test.com", "password": "114302ab"})

    response = test_client.get("/Institute_distribution")
    responses = test_client.post("/Institute_distribution", data={"Years": "1880"})

    assert b"UK distribution of public expenditure on education by spenders" in response.data
    assert b"TOTAL spendeing in thousands: 6278.022" in responses.data
    assert b"Data found!" in responses.data