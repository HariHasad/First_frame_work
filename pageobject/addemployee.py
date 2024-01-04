from selenium.webdriver.common.by import By


class Addemployees:
    def __init__(self, driver):
        self.driver = driver
    PIM_locator = (By.LINK_TEXT, "PIM")
    Addemplyesslink_locator = (By.LINK_TEXT, "Add Employee")
    Firstname_locator = (By.NAME, "firstName")
    Lastname_locator = (By.NAME, "lastName")
    loginSwitch_locator = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    Username_locator = (By.XPATH, "(//input[@autocomplete='off'])[1]")
    firstpassword_locator = (By.XPATH, "//input[@type='password']")
    confirmpassword_locator = (By.XPATH, "(//input[@type='password'])[2]")
    Savebtn_locator = (By.XPATH,"//button[@type='submit']")
    dropdown_locator = (By.CLASS_NAME, "oxd-userdropdown-tab")
    Logoutbtn_locator = (By.LINK_TEXT,"Logout")


    def PIMbtn(self):
        return self.driver.find_element(*Addemployees.PIM_locator)
    def Addempnavigation(self):
        return self.driver.find_element(*Addemployees.Addemplyesslink_locator)

    def Firstname(self):
        return self.driver.find_element(*Addemployees.Firstname_locator)
    def Lastname(self):
        return self.driver.find_element(*Addemployees.Lastname_locator)

    def loginswitch(self):
        return  self.driver.find_element(*Addemployees.loginSwitch_locator)
    def Username(self):
        return  self.driver.find_element(*Addemployees.Username_locator)
    def Firstpwd(self):
        return  self.driver.find_element(*Addemployees.firstpassword_locator)
    def COnfirmpwd(self):
        return  self.driver.find_element(*Addemployees.confirmpassword_locator)
    def Savebtn(self):
        return  self.driver.find_element(*Addemployees.Savebtn_locator)
    def Dropdown(self):
        return  self.driver.find_element(*Addemployees.dropdown_locator)

    def Logoutbtn(self):
        return  self.driver.find_element(*Addemployees.Logoutbtn_locator)



