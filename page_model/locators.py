from selenium.webdriver.common.by import By


class CommonLocators:
    """Rules for finding elements that appear on multiple pages"""

    MAIN_IFRAME = By.ID, 'bzeMainIframe'
    IFRAME_TITLE = By.TAG_NAME, 'title'


class TopNavigationLocators:
    """Rules for finding the elements of the top menu"""

    TOP_NAVIGATION = By.CLASS_NAME, 'bzeTopNavi'
    PAYMENTS_NAV = By.ID, 'bzeTopNaviPaymentSector'
    OFFERINGS_NAV = By.ID, 'bzeTopNaviProdukte'


class HeaderLocators:
    """Rules for finding the elements in the page header"""

    USER_MENU = By.ID, 'bzeContractNameMenu'


class OfferingsLocators:
    """Rules for finding the elements on the Offerings page"""

    TITLE = By.TAG_NAME, 'title'
    OVERVIEW = By.ID, 'naviItem_OVERVIEW'


class PaymentsLocators:
    """Rules for finding the elements related to payments"""

    PAYMENTS_MENU = By.XPATH, "//li[@id='bzeTopNaviPaymentSector']//div[@class='bzeTopNaviMenuContainer bzeTopNaviMenuContainerWithDa']"
    ACC_TRANSFER = By.ID, 'bzeTopNaviMenuEntryPaymentSingleAccountTransfer'
    PAYMENT_FORM_INPUT = By.CLASS_NAME, 'cgvCompressedFormEdit'
    PAYMENT_FORM_CHECK = By.CLASS_NAME, 'cgvCompressedFormCheck'
    PAYMENT_STATUS = By.XPATH, '/html[1]/body[1]/div[3]/div[2]/form[1]/div[5]/div[1]/fieldset[1]/div[1]/table[2]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[2]/span[2]'

    CREDIT_ACC_LIST = By.XPATH, '/html[1]/body[1]/div[3]/div[2]/form[1]/div[4]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]'
    CREDIT_ACC = By.CSS_SELECTOR, 'li[data-id="benAccountId"]'
    AMOUNT = By.NAME, 'i.amount.v'
    REASON_FOR_PAYMENT = By.NAME, 'i.reason.v'
    EXEC_DATE = By.NAME, 'i.valueDate.v'

    SUBMIT_BUTTON = By.ID, 'next'
    ERROR_CONTAINER = By.CLASS_NAME, 'cuiMessageWarningContainer'
    ERROR_MESSAGE = By.CLASS_NAME, 'uwrMessageBoxHeaderCompact'
