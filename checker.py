from playwright.sync_api import sync_playwright
import time

def check_cita():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Visit the DGT website (replace with actual URL)
        page.goto("https://www.dgt.es/es/tramites/cita-previa/")

        # Wait for the required element to load (replace with actual element)
        page.wait_for_selector("button#boton-cita")

        # Check if appointments are available
        if page.is_visible("button#boton-cita"):
            result = "Appointments are available!"
        else:
            result = "No appointments available."

        browser.close()
    return result

def periodic_check():
    while True:
        # Run the check every X minutes (e.g., every 5 minutes)
        result = check_cita()
        send_message(f"Cita check result: {result}")
        time.sleep(300)  # Sleep for 5 minutes before checking again
