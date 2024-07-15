from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd


class User:

    def __init__(self, driver):

        self.driver = driver

        # Open the login page
    
    def login(self, username, password):
        self.driver.get("https://sites.carleton.edu/manage/whmcs-admin/login.php")

        # Locate the login form elements
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        button.click()

    def submit(self):

        button = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save Changes']")
        button.click()

    def update_notes(self, id, notes):

        link = "https://sites.carleton.edu/manage/whmcs-admin/clientsprofile.php?userid=" + str(id)
        
        self.driver.get(link)

        admin_notes = self.driver.find_element(By.XPATH, "//textarea[@name='notes']")

        admin_notes.clear()

        admin_notes.send_keys(notes)

        self.submit()

    def update_group(self, id, group):

        link = "https://sites.carleton.edu/manage/whmcs-admin/clientsprofile.php?userid=" + str(id)

        self.driver.get(link)

        select = Select(self.driver.find_element(By.XPATH, '//select[@name="groupid"]'))

        options = select.options

        options_texts = [option.text for option in options]

        if group in options_texts:

            print("group found in select")
            
            select.select_by_visible_text(group)

            self.submit()

        else:

            print(f"Option {group} not found in the dropdown")   

    '''
    
    '''
    def update_domain(self, id, domain_id, domain):
            
        link = "https://sites.carleton.edu/manage/whmcs-admin/clientsservices.php?userid=" + str(id) + "productselect=" + str(domain_id)

        self.driver.get(link)
        
        domain_field = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='domain']")
            
        existing_domain = domain_field.get_attribute("value")
            
        if existing_domain != domain:
                
            domain_field.send_keys(domain)

            self.submit()

def main():

    username = input("Enter your username: ")

    password = input("Enter your password: ")

    file = input("Enter csv file name: ")

    driver = webdriver.Chrome()

    user = User(driver)

    user.login(username, password)

#     uncomment these codes and run the script to update user information. 

#     data = pd.read_csv(file)

#     for index, row in data.iterrows():

#         id = row[0]

#         group = row[4]

#         notes = row[5]

#         domain_id = row[6]

#         domain = row[7]

#         user.update_domain(id, domain_id, domain)
        
#         user.update_group(id, group)

#         user.update_notes(id, notes)


if __name__ == "__main__":
    main()



