*** Settings ***
Library    SeleniumLibrary
Library    browserstack_helper.py
Variables  ./testData.py
Variables  ./locators.py

*** Variables ***
${DEFAULT_BROWSER}    chrome

*** Keywords ***
Open Saucedemo
    [Arguments]    ${BROWSER}=${DEFAULT_BROWSER}
    Open Browserstack Browser    ${BROWSER}

Open Browserstack Browser
    [Arguments]    ${BROWSER}=chrome
    Create Browserstack Driver    ${BROWSER}
    Maximize Browser Window
    Go To    ${BASE_URL}
    Wait Until Page Contains Element    ${LOGIN_USERNAME_FIELD}

Login With Valid Credentials
    Input Text    ${LOGIN_USERNAME_FIELD}    ${USERNAME}
    Input Text    ${LOGIN_PASSWORD_FIELD}    ${PASSWORD}
    Click Button  ${LOGIN_BUTTON}
    Wait Until Page Contains Element    ${INVENTORY_TITLE}

Logout From Application
    Click Button    ${MENU_BUTTON}
    Wait Until Element Is Visible    ${LOGOUT_LINK}
    Click Element    ${LOGOUT_LINK}
    Wait Until Page Contains Element    ${LOGIN_BUTTON}

Close Browser Session
    Close Browser
