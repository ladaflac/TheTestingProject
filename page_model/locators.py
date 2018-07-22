from selenium.webdriver.common.by import By


class CommonLocators:
    """Rules for finding elements that appear on multiple pages"""

    MAIN_IFRAME = 'bzeMainIframe'


class TopNavigationLocators:
    """Rules for finding the elements of the top menu"""

    TOP_NAVIGATION = By.CLASS_NAME, 'bzeTopNavi'
    BUDGET_NAV = By.ID, 'bzeTopNaviBudgeting'
    PAYMENTS_NAV = By.ID, 'bzeTopNaviPaymentSector'
    OFFERINGS_NAV = By.ID, 'bzeTopNaviProdukte'


class HeaderLocators:
    """Rules for finding the elements in the page header"""

    USER_MENU = By.ID, 'bzeContractNameMenu'


class OfferingsLocators:
    """Rules for finding the elements on the Offerings page"""

    TITLE = By.TAG_NAME, 'title'
    OVERVIEW = By.ID, 'naviItem_OVERVIEW'
