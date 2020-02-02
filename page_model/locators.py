from selenium.webdriver.common.by import By


class CommonLocators:
    """Rules for finding elements that appear on multiple pages"""

    EBANKING_PAGE_TITLE = By.XPATH, '//h1[contains(text(),"E-Banking login")]'
    DEMO_APP_LINK = By.XPATH, '//a[contains(text(),"demo")]'

    WELCOME_MSG = By.XPATH, '//button[@class="Button__StyledButton-sc-13wwmgi-0 jjajkX"]'
    PAGE_TITLE = By.XPATH, '//h2[contains(text(),"Account and custody account overview")]'


class TopNavigationLocators:
    """Rules for finding the elements of the top menu"""

    TOP_NAVIGATION = By.TAG_NAME, 'ul'
    PAYMENTS_NAV = By.XPATH, '//nav//div[contains(text(),"Payments")]'
    # OFFERINGS_NAV = By.ID, 'bzeTopNaviProdukte'


class HeaderLocators:
    """Rules for finding the elements in the page header"""

    USER_MENU = By.CLASS_NAME, 'Avatar__StyledInitials-sc-1t1pqnp-1'


class HomepageLocators:
    """Rules for finding the elements of the homepage"""

    ACCOUNT_TABLE = By.XPATH, '//section[starts-with(@class,"AccountsList")][1]'
    ACCOUNT_ROW = By.XPATH, '//section[starts-with(@class,"AccountsList")]//div[starts-with(@class,"AccountInfoTile")]'
    ACCOUNT_TYPES = By.XPATH, '//h3[text()="Accounts"]/ancestor::section[starts-with(@class,"AccountsList__StyledAccountList")]//header/h3[starts-with(@class,"AccountInfoTile__StyledTitle")]'
    ACCOUNT_TYPES_xpath_only = ACCOUNT_TYPES[1]
    ACCOUNT_VALUE_TYPE = By.XPATH, '{}/ancestor::div[starts-with(@class,"AccountInfoTile__StyledAccountInfoTile")]//article[starts-with(@class,"AccountInfoTile__StyledFinancialInfo")]//span'.format(ACCOUNT_TYPES_xpath_only)


class PaymentsLocators:
    """Rules for finding the elements related to payments"""

    PAYMENTS_MENU_OPTIONS = By.XPATH, '//ul[starts-with(@class,"NavigationDropdownItem__StyledSubmenuList")]'
    ACC_TRANSFER = By.XPATH, '//ul[starts-with(@class,"NavigationDropdownItem__StyledSubmenuList")]/li/a[contains(@href,"account-transfer")]'
    PAYMENT_FORM_INPUT = By.XPATH, '//div[starts-with(@class,"Form__StyledForm")]'
    PAYMENT_FORM_CHECK = By.CLASS_NAME, 'cgvCompressedFormCheck'

    DEBIT_ACC_LIST = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledAccountSelect")][1]'
    DEBIT_ACC = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledAccountsList")]//li'
    CREDIT_ACC_LIST = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledEmpty")]'
    CREDIT_ACC = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledAccountsList")]//li'
    AMOUNT = By.XPATH, '//div[starts-with(@class,"InputAmount")]/input'
    REASON_FOR_PAYMENT = By.NAME, 'bookingText'
    EXEC_DATE = By.NAME, 'date'

    SUBMIT_BUTTON = By.XPATH, '//button//div[starts-with(text(),"Transfer")]'
    PAYMENT_STATUS_SUCCESS = By.XPATH, '//*[starts-with(text(),"Your order has been accepted")]'
    ERROR_CONTAINER = By.CLASS_NAME, 'cuiMessageWarningContainer'
    ERROR_MESSAGE = By.XPATH, '//*[starts-with(text(),"Please fill out this field")]'


# not used anymore - offerings removed from the demo application
# class OfferingsLocators:
#     """Rules for finding the elements on the Offerings page"""
#
#     TITLE = By.TAG_NAME, 'title'
#     OVERVIEW = By.ID, 'naviItem_OVERVIEW'
