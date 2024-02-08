from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

def espn():
    website = 'https://www.espn.com/college-sports/basketball/recruiting/playerrankings'
    driver = webdriver.Chrome()

    driver.get(website)

    print(driver.title)

    players = driver.find_elements(By.XPATH, "//div[contains(@class, 'name')]//strong")

    players_result = ['ESPN']

    for i in range(50):
        players_result.append(players[i].text)

    df_data=pd.DataFrame(players_result)
    df_data.to_csv('espn.csv', index= False, header=False)

    df_data.index = np.arange(1, len(df_data) + 1)
