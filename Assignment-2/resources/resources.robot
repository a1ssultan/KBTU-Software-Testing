*** Settings ***
Library    SeleniumLibrary
Variables  ./testData.py
Variables  ./locators.py

*** Keywords ***
Open Saucedemo
    Open Browser    ${BASE_URL}    chrome
    Maximize Browser Window
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
