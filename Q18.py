
# Import required Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()

try:
    # Step 2: Open DemoQA Text Box webpage
    driver.get("https://demoqa.com/text-box")

    # Maximize the browser window
    driver.maximize_window()

    # Step 3: Wait until the form is loaded
    wait = WebDriverWait(driver, 10)

    # Step 4: Enter user's full name
    name = wait.until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    name.send_keys("Anand Krishna")

    # Step 5: Enter email address
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("anand@gmail.com")

    # Step 6: Enter current address
    current_address = driver.find_element(
        By.ID, "currentAddress"
    )
    current_address.send_keys("Thrissur, Kerala")

    # Step 7: Enter permanent address
    permanent_address = driver.find_element(
        By.ID, "permanentAddress"
    )
    permanent_address.send_keys("Koorkenchery, Thrissur")

    # Step 8: Find the Submit button
    submit_button = driver.find_element(By.ID, "submit")

    # Center the button in the viewport to avoid fixed page overlays
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        submit_button
    )
    wait.until(EC.element_to_be_clickable((By.ID, "submit")))

    # Click the Submit button
    try:
        submit_button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", submit_button)

    # Step 9: Wait until submitted details are displayed
    output = wait.until(
        EC.visibility_of_element_located((By.ID, "output"))
    )

    # Step 10: Extract submitted details
    output_name = driver.find_element(
        By.ID, "name"
    ).text

    output_email = driver.find_element(
        By.ID, "email"
    ).text

    output_current_address = driver.find_element(
        By.CSS_SELECTOR, "#output #currentAddress"
    ).text

    output_permanent_address = driver.find_element(
        By.CSS_SELECTOR, "#output #permanentAddress"
    ).text

    # Step 11: Verify entered details
    if (
        output_name == "Name:Anand Krishna"
        and output_email == "Email:anand@gmail.com"
        and output_current_address == "Current Address :Thrissur, Kerala"
        and output_permanent_address == "Permananet Address :Koorkenchery, Thrissur"
    ):
        print("Data entered successfully!")
        print("All details verified successfully!")

    else:
        print("Data verification failed!")

    # Display submitted details
    print("\nSubmitted Details:")
    print(output_name)
    print(output_email)
    print(output_current_address)
    print(output_permanent_address)

finally:
    # Step 12: Close the browser
    driver.quit()
    print("\nBrowser closed successfully!")
