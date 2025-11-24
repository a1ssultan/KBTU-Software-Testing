from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.common.exceptions import WebDriverException
from robot.libraries.BuiltIn import BuiltIn
import warnings


def get_browserstack_remote_url():
    """Returns the BrowserStack remote URL."""
    username = "bsuser_LicKpW"
    access_key = "fUtAHKsD4ZX9TEkGVrPe"
    return f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"


def get_browserstack_capabilities(browser: str):
    """
    Returns BrowserStack capabilities as a dictionary.
    
    Args:
        browser: Browser name (chrome, firefox, or safari)
    
    Returns:
        Dictionary with BrowserStack capabilities
    """
    browser_lower = browser.lower()
    if browser_lower == "chrome":
        browser_name = "Chrome"
    elif browser_lower == "firefox":
        browser_name = "Firefox"
    elif browser_lower == "safari":
        browser_name = "Safari"
    else:
        browser_name = "Chrome"
    
    capabilities = {
        "browserName": browser_name,
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Sonoma",
            "projectName": "KBTU Software Testing HW3+4",
            "buildName": "Robot Tests Build",
            "sessionName": f"{browser_name} automated test",
            "seleniumVersion": "4.25.0"
        }
    }
    
    return capabilities


def get_browserstack_options(browser: str):
    """
    Returns BrowserStack options for the specified browser.
    
    Args:
        browser: Browser name (chrome, firefox, or safari)
    
    Returns:
        Options object configured for BrowserStack
    """
    browser_lower = browser.lower()
    if browser_lower == "chrome":
        browser_name = "Chrome"
        options = ChromeOptions()
    elif browser_lower == "firefox":
        browser_name = "Firefox"
        options = FirefoxOptions()
    elif browser_lower == "safari":
        browser_name = "Safari"
        options = SafariOptions()
    else:
        browser_name = "Chrome"
        options = ChromeOptions()
    
    # BrowserStack capabilities
    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", "latest")
    options.set_capability("bstack:options", {
        "os": "OS X",
        "osVersion": "Sonoma",
        "projectName": "KBTU Software Testing HW3+4",
        "buildName": "Robot Tests Build",
        "sessionName": f"{browser_name} automated test",
        "seleniumVersion": "4.25.0"
    })
    
    return options


def create_browserstack_driver(browser: str) -> WebDriver:
    """
    Creates a Selenium remote driver for BrowserStack.
    Falls back to local driver if BrowserStack is unavailable.
    Registers the driver with SeleniumLibrary automatically.
    
    Args:
        browser: Browser name (chrome, firefox, or safari)
    
    Returns:
        WebDriver instance configured for BrowserStack or local
    """
    remote_url = get_browserstack_remote_url()
    options = get_browserstack_options(browser)
    
    browser_lower = browser.lower()
    if browser_lower == "chrome":
        browser_name = "Chrome"
    elif browser_lower == "firefox":
        browser_name = "Firefox"
    elif browser_lower == "safari":
        browser_name = "Safari"
    else:
        browser_name = "Chrome"
    
    # Try to create BrowserStack driver, fallback to local if it fails
    try:
        # Suppress the warning about embedding credentials in URL
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )
        # Register the driver with SeleniumLibrary
        _register_driver_with_seleniumlibrary(driver)
        return driver
    except (WebDriverException, Exception) as e:
        # If BrowserStack fails (e.g., time expired, connection issue), use local driver
        print(f"BrowserStack unavailable ({str(e)}). Falling back to local {browser_name} driver.")
        
        # Create fresh options for local driver (without BrowserStack capabilities)
        if browser_lower == "chrome":
            local_options = ChromeOptions()
            driver = webdriver.Chrome(options=local_options)
        elif browser_lower == "firefox":
            local_options = FirefoxOptions()
            driver = webdriver.Firefox(options=local_options)
        elif browser_lower == "safari":
            local_options = SafariOptions()
            driver = webdriver.Safari(options=local_options)
        else:
            local_options = ChromeOptions()
            driver = webdriver.Chrome(options=local_options)
        
        # Register the driver with SeleniumLibrary
        _register_driver_with_seleniumlibrary(driver)
        return driver


def _register_driver_with_seleniumlibrary(driver: WebDriver):
    """Register a WebDriver instance with SeleniumLibrary."""
    try:
        builtin = BuiltIn()
        selenium_library = builtin.get_library_instance('SeleniumLibrary')
        
        # Get the driver manager
        driver_manager = selenium_library._drivers
        
        # Ensure _drivers list exists
        if not hasattr(driver_manager, '_drivers') or driver_manager._drivers is None:
            driver_manager._drivers = []
        
        # Add driver to the list
        driver_manager._drivers.append(driver)
        
        # Set as current driver
        driver_manager._current_index = len(driver_manager._drivers) - 1
        driver_manager.current = driver
        
        # Update cache if it exists
        if hasattr(driver_manager, '_cache') and driver_manager._cache is not None:
            try:
                driver_manager._cache.current = driver
            except:
                pass
                
    except Exception as e:
        # If registration fails, try to at least set the current driver
        try:
            builtin = BuiltIn()
            selenium_library = builtin.get_library_instance('SeleniumLibrary')
            # Try to directly set current driver
            selenium_library._drivers.current = driver
        except Exception as e2:
            # If all else fails, print warning
            # The driver is still created and can be used, but SeleniumLibrary might not manage it
            pass  # Silently fail - driver will still work

