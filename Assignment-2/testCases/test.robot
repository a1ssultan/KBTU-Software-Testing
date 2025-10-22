*** Settings ***
Library    SeleniumLibrary
Library    Collections
Documentation     Automated Test Cases for Saucedemo Website
Resource          ../resources/resources.robot

*** Test Cases ***

Login Test
    [Tags]    smoke
    Open Saucedemo
    Login With Valid Credentials
    Page Should Contain Element    ${INVENTORY_TITLE}
    Close Browser Session


Invalid Login Test
    [Tags]    negative
    Open Saucedemo
    Input Text    ${LOGIN_USERNAME_FIELD}    wrong_user
    Input Text    ${LOGIN_PASSWORD_FIELD}    wrong_pass
    Click Button  ${LOGIN_BUTTON}
    Page Should Contain Element    ${LOGIN_ERROR_MESSAGE}
    Close Browser Session


Add Product To Cart
    [Tags]    regression
    Open Saucedemo
    Login With Valid Credentials
    Click Button    ${ADD_TO_CART_BUTTON}
    Click Element   ${CART_ICON}
    Page Should Contain Element    ${ITEM_NAME}
    Close Browser Session


Remove Product From Cart
    [Tags]    regression
    Open Saucedemo
    Login With Valid Credentials
    Click Button    ${ADD_TO_CART_BUTTON}
    Click Element   ${CART_ICON}
    Click Button    ${REMOVE_BUTTON}
    Element Should Not Be Visible    ${ITEM_NAME}
    Close Browser Session


Logout Test
    [Tags]    smoke
    Open Saucedemo
    Login With Valid Credentials
    Logout From Application
    Page Should Contain Element    ${LOGIN_BUTTON}
    Close Browser Session


Verify Product Sorting Low To High
    [Tags]    regression
    Open Saucedemo
    Login With Valid Credentials
    Wait Until Element Is Visible    xpath://select[@data-test='product-sort-container']    timeout=5s
    Select From List By Value        xpath://select[@data-test='product-sort-container']    lohi
    Sleep    2s
    ${prices}=    Get WebElements    xpath://div[@class='inventory_item_price']
    ${price_values}=    Create List
    FOR    ${price}    IN    @{prices}
        ${text}=    Get Text    ${price}
        ${num}=    Evaluate    float("${text}".replace("$", ""))
        Append To List    ${price_values}    ${num}
    END
    ${sorted}=    Evaluate    sorted(${price_values})
    Should Be Equal As Numbers    ${price_values[0]}    ${sorted[0]}
    Should Be Equal    ${price_values}    ${sorted}
    Close Browser Session


Add Multiple Products To Cart
    [Tags]    regression
    Open Saucedemo
    Login With Valid Credentials
    Click Button    id:add-to-cart-sauce-labs-backpack
    Click Button    id:add-to-cart-sauce-labs-bike-light
    Click Button    id:add-to-cart-sauce-labs-bolt-t-shirt
    ${badge}=    Get Text    xpath://span[@class='shopping_cart_badge']
    Should Be Equal As Integers    ${badge}    3
    Click Element   ${CART_ICON}
    ${items}=    Get Element Count    xpath://div[@class='cart_item']
    Should Be Equal As Integers    ${items}    3
    Close Browser Session


UI Elements Visibility Test
    [Tags]    smoke
    Open Saucedemo
    Login With Valid Credentials
    Page Should Contain Element    xpath://div[@class='app_logo']
    Page Should Contain Element    xpath://div[@class='inventory_list']
    Page Should Contain Element    xpath://div[@class='shopping_cart_container']
    Close Browser Session
