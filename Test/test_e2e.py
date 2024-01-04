import time

from selenium.webdriver.support.wait import WebDriverWait

from pageobject.addemployee import Addemployees
from pageobject.login import Loginpage
from utilities.BaseClass import Baseclass
import mysql.connector

class Teststart(Baseclass):
   def test_loginpage_case(self):

        log = self.getLogger()
        # Here DB connection
        con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
        curs = con.cursor()
        curs.execute("select * from staff;")

        for row in curs:
         userN = row[0]
         Passwd = row[1]

        loginpageUN = Loginpage(self.driver)
        loginpageUN.userName().send_keys(userN)
        loginpagepw = Loginpage(self.driver)
        loginpagepw.passwd().send_keys(Passwd)
        loginbutton = Loginpage(self.driver)
        loginbutton.loginbtn()
        log.info("Log one: Succesfully logged into home page")
        # Here DB will be closed
        con.close()
   def test_addemployee_case(self):
        log = self.getLogger()
        addemp = Addemployees(self.driver)
        addemp.PIMbtn().click()
        log.info("Log two: Succesfully logged into add employee page")
        addempone = Addemployees(self.driver)
        addempone.Addempnavigation().click()
        FirstNamefield = Addemployees(self.driver)
        FirstNamefield.Firstname().send_keys("jin")
        LastNamefield = Addemployees(self.driver)
        LastNamefield.Lastname().send_keys("one")
        loginSwitch = Addemployees(self.driver)
        loginSwitch.loginswitch().click()
        UserNamefiled = Addemployees(self.driver)
        UserNamefiled.Username().send_keys("USERYAMAHA")
        FirstPWD = Addemployees(self.driver)
        FirstPWD.Firstpwd().send_keys("Hari@1234$")
        FinalPWD = Addemployees(self.driver)
        FinalPWD.COnfirmpwd().send_keys("Hari@1234$")
        Savebutton = Addemployees(self.driver)
        Savebutton.Savebtn().click()
        log.info("Log three: Succesfully added new staff")
        time.sleep(5)
        Dropdwn = Addemployees(self.driver)
        Dropdwn.Dropdown().click()
        time.sleep(5)
        LogoutBTN = Addemployees(self.driver)
        LogoutBTN.Logoutbtn().click()
        log.info("Log four: Succesfully logged out")


   def test_final_logout_case(self):
        log = self.getLogger()
        Actual_homepage_title = self.driver.title
        print("Actual tile :" + Actual_homepage_title)
        Expected_homepage_title = "OrangeHRM"
        print("Expected title :" + Expected_homepage_title)
        if Actual_homepage_title == Expected_homepage_title:
          print("Successfully logged out")
        else:
          print("failed to log out")













