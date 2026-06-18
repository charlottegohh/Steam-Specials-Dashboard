def scrape_steam(): 
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    import time

    #run in headless mode
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    #open steam specials page
    url = "https://store.steampowered.com/search/?specials=1"
    driver.get(url)

    #wait for page to load
    time.sleep(5)

    #add scrolling
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    #find all game elements
    games = driver.find_elements(By.CLASS_NAME, "search_result_row")

    data = []

    for game in games[:50]: #limit to first 50
        try:
            title = game.find_element(By.CLASS_NAME, "title").text
            original_price = game.find_element(By.CLASS_NAME, "discount_original_price").text
            discount = game.find_element(By.CLASS_NAME, "discount_pct").text
            price = game.find_element(By.CLASS_NAME, "discount_final_price").text

            data.append({
                "title": title,
                "original_price": original_price,
                "discount": discount,
                "price": price
            })
        except Exception as e:
            print("Error:", e)
            continue

    driver.quit()
    return data