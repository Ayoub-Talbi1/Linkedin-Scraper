from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys

with open('credentials.txt', 'r') as file:
    email = file.readline().strip()
    passwd = file.readline().strip()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get("https://fr.linkedin.com/")
time.sleep(1)
mail = driver.find_element(By.ID, "session_key")
mail.send_keys(email)
password = driver.find_element(By.ID, "session_password")
password.send_keys(passwd)
password.send_keys(Keys.RETURN)
time.sleep(1)
''''try:
    recherche = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input"))
    )
    recherche.clear()
    recherche.send_keys("web developer")
    recherche.send_keys(Keys.ENTER)

except:
    driver.quit()
time.sleep(2)
try:
    Search_list = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "search-reusables__primary-filter"))
    )
    time.sleep(1)
    people_button = Search_list[3].find_element(By.TAG_NAME, "button")
    time.sleep(1)
    people_button.click()
except:
    driver.quit()
'''''
########################################--------BASIC-FILTERS----------#############################################
input_values = [sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8],
                sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13]]

print(input_values)

connection_to_relation = {"1st": "F", "2nd": "S", "3rd+": "O", "1st & 2nd": "F S", "1st & 3rd+": "F O",
                          "2nd & 3rd+": "S O", "All": "F S O", "": ""}
language_to_langue = {"English": "en", "French": "fr", "Portuguese": "pt", "Spanish": "es", "Others": "_o", "": ""}
member_to_member = {"Joining a nonprofit board": "boardMember", "Pro bono consulting and volunteering": "proBono",
                    "Both": "boardMember proBono", "": ""}
relation = connection_to_relation[input_values[0]]
l = language_to_langue[input_values[9]]
member = member_to_member[input_values[10]]


def a_lecoute_de(member):
    s = member.split()
    if len(s) == 0:
        return ""
    r = "contactInterest=%5B\""
    for i in range(len(s)):
        if i != len(s) - 1:
            r += s[i] + "\"%2C\""
        else:
            r += s[i] + "\"%5D"
    return "&" + r


def relations(relation):
    s = relation.split()
    if len(s) == 0:
        return ""
    r = "network=%5B\""
    for i in range(len(s)):
        if i != len(s) - 1:
            r += s[i] + "\"%2C\""
        else:
            r += s[i] + "\"%5D"
    return "&" + r


def langue(l):
    s = l.split()
    if len(s) == 0:
        return ""
    r = "profileLanguage=%5B\""
    for i in range(len(s)):
        if i != len(s) - 1:
            r += s[i] + "\"%2C\""
        else:
            r += s[i] + "\"%5D"
    return "&" + r


driver.get("https://www.linkedin.com/search/results/people/?keywords="+sys.argv[1].replace(" ", "%20") + relations(relation) + langue(
    l) + a_lecoute_de(member) + "&origin=FACETED_SEARCH")

############################################------ALL-FILTERS-BUTTON------####################################################

try:
    all_filters = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/section[1]/div[1]/nav[1]/div[1]/div[1]/div[1]/button[1]"))
    )
    all_filters.click()
except:
    driver.quit()

#############################################-----------FILTERS-----------#################################################

try:
    Filters = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "search-reusables__secondary-filters-filter"))
    )

    for i in list(range(1, 9)) + [11]:
        time.sleep(1)
        ul = Filters[i].find_element(By.TAG_NAME, "ul")
        time.sleep(1)
        lis = ul.find_elements(By.TAG_NAME, "li")
        time.sleep(1)
        button = lis[-1].find_element(By.TAG_NAME, "button")
        button.click()
        time.sleep(1)
        input_ = lis[-1].find_element(By.TAG_NAME, "input")
        time.sleep(1)
        input_.send_keys(input_values[i])
        time.sleep(1)
        input_.send_keys(Keys.DOWN)
        time.sleep(1)
        input_.send_keys(Keys.RETURN)
except:
    driver.quit()
time.sleep(1)

####################################---------------RESULTS-BUTTON----------------##########################################

try:
    button = WebDriverWait(input_, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/button[2]"))
    )
    button.click()
except:
    driver.quit()

####################################-----------------MESSAGE-------------------#############################################
url=str(driver.current_url)
page=1
url+="&page="+str(page)
def get_url(url,page):
    return url.split("&page=")[0]+"&page="+str(page)
time.sleep(1)
divs=driver.find_element(By.CLASS_NAME,"search-results-container").find_elements(By.TAG_NAME,"div")
time.sleep(1)
ul=divs[2].find_element(By.TAG_NAME,"ul")
time.sleep(1)
li_elements = ul.find_elements(By.TAG_NAME, "li")
time.sleep(1)
for j in range(100):
    for i in range(len(li_elements)):
        try:
            li_elements[i].find_element(By.TAG_NAME,"button").click()
            try:
                text = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[5]/aside[1]/div[2]/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/p[1]"))
                )
                text.send_keys(sys.argv[14])
                time.sleep(1)
                send_button=driver.find_element(By.XPATH,"/html[1]/body[1]/div[5]/aside[1]/div[2]/div[2]/form[1]/footer[1]/div[2]/div[1]/button[1]")
                send_button.click()
            except:
                pass
            time.sleep(1)
            try:
                active_element = driver.switch_to.active_element
                active_element.click()
                time.sleep(1)
                active_element.send_keys(Keys.ESCAPE)
            except:
                driver.quit()
        except:
            continue
    driver.get(get_url(url,page))
    page+=1
