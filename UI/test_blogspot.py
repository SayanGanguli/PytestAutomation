import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_verifyTitle(setUp):
    assert setUp.title == "Automation Testing Practice"

def test_textbox(setUp):
    setUp.find_element(By.ID,"name").send_keys("John Wick")
    setUp.find_element(By.ID,"email").send_keys("jw@email.com")
    setUp.find_element(By.ID,"phone").send_keys("5612786800")
    setUp.find_element(By.ID,"textarea").send_keys("Manhattan, New York")

def test_radiobutton_checkbox(setUp):
    setUp.find_element(By.ID,"male").click()
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for day in days:
        setUp.find_element(By.ID,f'{day.lower()}').click()

def test_perform_dropdown(setUp):
    country = setUp.find_element(By.ID,"country")
    select1 = Select(country)
    select1.select_by_visible_text("Australia")

    colors = setUp.find_element(By.ID,"colors")
    select2 = Select(colors)
    select2.select_by_visible_text("Red")
    select2.select_by_visible_text("Yellow")
    select2.select_by_visible_text("White")
    time.sleep(5)
    selected_options = [opt.text for opt in select2.all_selected_options]
    print(selected_options)
    assert "Red" in selected_options
    assert "Yellow" in selected_options
    select2.deselect_all()
    selected_options = [opt.text for opt in select2.all_selected_options]
    print(selected_options)

def test_perform_date_picker(setUp):
    # First Date Picker :::: Selecting 15/02/2022
    # Open the date picker widget
    date_picker1 = setUp.find_element(By.ID, "datepicker")
    date_picker1.click()
    time.sleep(1)

    # Navigate back until we reach February 2004
    while True:
        month = setUp.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        year = setUp.find_element(By.CLASS_NAME, "ui-datepicker-year").text
        if month == "February" and year == "2022":
            break
        setUp.find_element(By.CLASS_NAME, "ui-datepicker-prev").click()
        time.sleep(0.2)

    # Select day 15
    setUp.find_element(By.XPATH, "//a[text()='15']").click()
    time.sleep(2)

    # Assertion
    assert date_picker1.get_attribute("value") == "02/15/2022"

    #Second Date Picker:::: Selecting 08/11/2016
    setUp.find_element(By.ID,"txtDate").click()
    wait = WebDriverWait(setUp, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-month")))










