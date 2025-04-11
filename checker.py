import time
from playwright.sync_api import sync_playwright

# Function to check if there's a cita
def check_cita():
    print("Checking cita...")  # Debugging line to confirm function is being called
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Headless mode means no UI
        page = browser.new_page()
        page.goto("https://sedeclave.dgt.gob.es/WEB_NCIT_CONSULTA/solicitarCita.faces")

        # Check for captcha
        if page.query_selector('iframe[src*="recaptcha"]'):
            print("Captcha detected!")  # Debugging line to confirm captcha detection
            return "Captcha detected"
        
        # Continue with the normal process (Selecting province, country, etc)
        # Your logic here for selecting options and checking citas
        # For now, we'll just simulate checking and return a mock response
        
        if "No hay citas" in page.content():
            print("No citas available")  # Debugging line for availability check
            return "No citas available"
        else:
            print("Citas available")  # Debugging line for availability check
            return "Citas available"

        browser.close()

# Periodically check every 30 minutes
def periodic_check():
    while True:
        result = check_cita()
        print(f"Result: {result}")
        time.sleep(1800)  # Sleep for 30 minutes
