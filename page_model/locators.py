from selenium.webdriver.common.by import By


class CommonLocators:
    """Rules for finding elements that appear on multiple pages"""

    MAIN_IFRAME = By.ID, 'bzeMainIframe'
    IFRAME_TITLE = By.TAG_NAME, 'title'
    APP_NAME = By.TAG_NAME, 'h1'
    WELCOME_MSG = By.XPATH, '//button[@class="Button__StyledButton-sc-13wwmgi-0 jjajkX"]'
    PAGE_TITLE = By.TAG_NAME, 'h2'


class TopNavigationLocators:
    """Rules for finding the elements of the top menu"""

    TOP_NAVIGATION = By.TAG_NAME, 'ul'
    PAYMENTS_NAV = By.ID, 'bzeTopNaviPaymentSector'
    PAYMENTS_NAV = By.XPATH, '//nav//div[contains(text(),"Payments")]'
    # OFFERINGS_NAV = By.ID, 'bzeTopNaviProdukte'


class HeaderLocators:
    """Rules for finding the elements in the page header"""

    USER_MENU = By.CLASS_NAME, 'Avatar__StyledInitials-sc-1t1pqnp-1'


# not used anymore - offerings removed from the demo application
class OfferingsLocators:
    """Rules for finding the elements on the Offerings page"""

    TITLE = By.TAG_NAME, 'title'
    OVERVIEW = By.ID, 'naviItem_OVERVIEW'


class PaymentsLocators:
    """Rules for finding the elements related to payments"""

    ACC_TRANSFER = By.XPATH, '//a[@href="/microsites/digital-ebanking-demo/en/payments/account-transfer"]'
    PAYMENT_FORM_INPUT = By.XPATH, '//div[starts-with(@class,"Form__StyledForm")]'
    PAYMENT_FORM_CHECK = By.CLASS_NAME, 'cgvCompressedFormCheck'

    DEBIT_ACC_LIST = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledAccountSelect")][1]'
    DEBIT_ACC = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledAccountsList")]//li'
    CREDIT_ACC_LIST = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledEmpty")]'
    CREDIT_ACC = By.XPATH, '//div[starts-with(@class,"AccountSelect__StyledAccountsList")]//li'
    AMOUNT = By.XPATH, '//div[starts-with(@class,"InputAmount")]/input'
    REASON_FOR_PAYMENT = By.NAME, 'i.reason.v'
    EXEC_DATE = By.NAME, 'date'

    SUBMIT_BUTTON = By.XPATH, '//button//div[starts-with(text(),"Transfer")]'
    PAYMENT_STATUS_SUCCESS = By.XPATH, '//*[starts-with(text(),"Your order has been accepted")]'
    ERROR_CONTAINER = By.CLASS_NAME, 'cuiMessageWarningContainer'
    ERROR_MESSAGE = By.XPATH, '//*[starts-with(text(),"Please fill out this field")]'
