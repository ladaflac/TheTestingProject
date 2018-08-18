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

    SUBMIT_BUTTON = By.ID, 'next'
    ERROR_CONTAINER = By.CLASS_NAME, 'cuiMessageWarningContainer'
    ERROR_MESSAGE = By.CLASS_NAME, 'uwrMessageBoxHeaderCompact'
