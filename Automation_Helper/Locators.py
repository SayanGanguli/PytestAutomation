from selenium.webdriver.common.by import By


def getLocator(by_loc=""):
    if by_loc.lower() == "xpath":
        return By.XPATH
    elif by_loc.lower() == "css":
        return By.CSS_SELECTOR
    elif by_loc.lower() == "id":
        return By.ID
    elif by_loc.lower() == "name":
        return By.NAME
    elif by_loc.lower() == "link":
        return By.LINK_TEXT
    else:
        return False


### LoginPage ###
login_register_button = "//div[@class='SSOLogin__Container']/button"
login_Button = "//button[@type='submit']"
logout_Button = "//div[@class='dropdown-panel is-open']/div/button"
account_Icon = "//button[@aria-label='profile dropdown']"

### Cookies Banner ###
cookies_banner = "_evidon_banner"
accepting_cookies = "_evidon-accept-button"

### Home Page ###
purchase_order_link = "div[class='PrintInfo__text']"
last_order_details = "div[class='ProfileOrderDetailsContainer-header'] h3"
recent_order_button = "//tbody[@class='ProfileRecentOrders__tableBody']/tr[1]/td[4]/button"

### Product Main Page ###
product_page = "//span[@class='redcontentsmallbanner']"
navigation_list = "//li[@class='Nav-list']/a"
add_to_cart = "(//span[@class='add-to-basket--cta-text'])[2]"
view_cart = "//div[@class='dropdown dropdown--cart dropdown--hover']/button"
order_desktop_view = "(//div[@class='addtional_order desktop_view'])[1]"
checkout_button = "//div[@class='CheckoutButton']"
address_ddn = "//div[@class='CheckoutAddressBook__Select']/div"
address1 = "//span[@id='dropdown-account-address-0']"
purchase_number = "//input[@name='cx_poNumber']"
tc_checkbox = "//input[@id='CheckoutAgreementTerms']"
order_request = "//div[contains(@class,'Checkout')]/button[2]"
order_confirmation = "(//div[@class = 'OrderAck__orderMessage'])[1]"
fetch_order_no = order_confirmation + "/font/span/font"
device_configure_button = "//div[@class='ProductPrice_Button']/button"

order_account_name = "cc-orderDetails-accountName-value"
order_user_lastname = "cc-orderDetails-lastName-value"
order_user_firstname = "cc-orderDetails-firstName-value"
order_user_email = "cc-orderDetails-customerEmail-value"
order_totalValue = "cc-orderDetails-total-value"
agent_ordersearch_menu = "//li[@id='AgentOrderSearch']/a"
compare_price_button = "//button[contains(@class,'comparePriceButtonText')]"
order_details_info = "//td[contains(@class,'ProFormaInvoice__RefValue')]"
fetched_order_no = "//div[@class='ProFormaInvoice__HeadingValue label1']"
fetched_invoice_no = "(//p[@class='Delivery__shippingMethod textProp'])[2]"
allcomparison_remove_button = "//div[contains(@class,'multipleProductsCompareButton')]/div"
compare_products_button = "//div[contains(@class,'multipleProductsCompareButton')]/a"
configurator_modal_close_icon = "//div[@id='bundle-selector-main']/div/span[@class='bundle-selector-close-x icon-cross']"
add_compare_button = "i[class = 'icon btn--icon icon-arrow-left-right']"
remove_configuration_button = "a[class = 'bundle-selector--clear-all blueLight']"


### Email Page ###
enter_email = "//input[@id='login']"
arrow_button = "refreshbut"
mail_body_frame = "ifmail"
mail_body_content = "//body[@class='bodymail yscrollbar']/header"

### OCC Page ###
occ_signin_button = "//span[text()='Sign In']"
occ_dashboard_page = "//h1[text()='Welcome to your Dashboard']"
orderid_field = "//input[@name='orderIdText']"
order_search_button = "cc-search-button"
order_reset_button = "cc-reset-button"
order_search_result = "cc-order-search-result"
searchtable_columnheads = "//table[@id='cc-order-search-results']/thead/tr/th"
searchtable_rowvalues = "//table[@id='cc-order-search-results']/tbody/tr/td"
print_confirmation_button = "//button[text()='Print Confirmation']"
filter_catalog_field = "//input[@placeholder = 'Filter for products']"
filter_account_field = "//input[@placeholder='Filter for contact or email']"
role_No_Company = "//a[@title='NO Company']/following::span[2]"
filtered_account = "//span[@data-bind='text: $data.lastName']"
catalog_ddn_button = "cc-list-catalogs_current-value-btn|text"
filter_pricegroup_menu = "//input[@placeholder='Search for a price group']"
edit_catalog_icon = "//span[@class='oj-ux-ico-edit' and @slot]"
product_modal_menu = "cc-productDetails-close"
edit_pricegroup_icon = "//span[@class='oj-button-icon oj-start oj-ux-ico-edit']"
price_modal_window = "cc-edit-product-prices-modal-root"
min_range_slot1 = "//tr[@class='range']/td/span[@data-bind='text: levelMinimum()']"
max_range_slot1 = "//div[@class='oj-text-field-readonly' and @role='textbox']"
min_range_slot2 = "//input[@aria-label='Level minimum']"
account_topmenu_icon = "//*[@background='purple']"
occ_logout_Button = "//a[text()='Logout']"


### Registration Page ####
register_link = "//div[contains(@class,'signup')]/following::a[2]"
select_country_ddn = "//b[text()='Country']/following::button[1]"
select_language_ddn = "//b[text()='Country']/following::button[2]"
