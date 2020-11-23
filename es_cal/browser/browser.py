from selenium import webdriver
import os

# old method using selenium webbrowser
def make_webdriver_old():
    try:
        from pyvirtualdisplay import Display
        from selenium import webdriver

        display = Display(visible=0, size=(800, 600))
        display.start()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()
    except ImportError as e:
        print(e)
        # Load webdriver
        from selenium import webdriver

        driver = webdriver.Chrome()
    return driver


# new method using


def make_webdriver(build_name="Earnings-stock-calendar"):
    remote_url = os.environ.get("REMOTE_SELENIUM_URL")
    if remote_url == None:
        raise Exception("Missing CALENDAR_ID in env vars")
    desired_cap = {
        "os_version": "10",
        "resolution": "1920x1080",
        "browser": "Chrome",
        "browser_version": "latest",
        "os": "Windows",
        "name": "ES-Calendar-[Python]",  # test name
        "build": build_name,  # CI/CD job or build name
    }
    driver = webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=desired_cap,
    )
    return driver
