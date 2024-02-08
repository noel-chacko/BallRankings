from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def on3():
    website = 'https://www.on3.com/db/rankings/industry-player/basketball/2024/'
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(50)

    driver.get(website)

    print(driver.title)

    # Find player elements
    players = driver.find_elements(By.XPATH, "//a[contains(@class, 'MuiTypography-root MuiTypography-h5 MuiLink-root MuiLink-underlineHover css-1rtd33f')]")

    players_result = ['On3']

    # Loop over the actual number of players found
    for i in range(min(50, len(players))):
        players_result.append(players[i].text)

    df_data = pd.DataFrame(players_result)
    df_data.to_csv('on3.csv', index=False, header=False)

    driver.close()  # It's a good practice to close the driver after the task is done