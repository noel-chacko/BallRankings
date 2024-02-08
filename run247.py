from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def run247():

    website = 'https://247sports.com/Season/2024-Basketball/RecruitRankings/?InstitutionGroup=HighSchool/'
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(40)

    driver.get(website)

    print(driver.title)

    players = driver.find_elements(By.XPATH, "//a[contains(@class,'rankings-page__name-link')]")

    players_result = ['24/7']

    for i in range(50):
        players_result.append(players[i].text)

    df_data=pd.DataFrame(players_result)
    df_data.to_csv('247.csv', index= False, header=False)