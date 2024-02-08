from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
def rivals():
    website = 'https://rivals.rivals.com/prospect_rankings/rivals150/2024?position=ALL%20POSITIONS'
    driver = webdriver.Chrome()

    driver.get(website)

    print(driver.title)

    firsts = driver.find_elements(By.XPATH, "//div[@class='first-name ng-binding']")
    lasts = driver.find_elements(By.XPATH, "//div[@class='last-name ng-binding']")

    players_result = ['Rivals']

    for i in range(50):
        x = firsts[i].text.title()
        y = lasts[i].text.title()
        players_result.append(x + " " + y)

    df_data=pd.DataFrame(players_result)
    df_data.to_csv('rivals.csv', index= False, header=False)
