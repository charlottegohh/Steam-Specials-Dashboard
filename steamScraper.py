def scrape_steam():
    import requests
    from bs4 import BeautifulSoup

    url = "https://store.steampowered.com/search/?specials=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    games = soup.find_all("a", class_="search_result_row")

    data = []

    for game in games[:50]:
        try:
            title = game.find(class_="title").text
            discount = game.find(class_="discount_pct").text
            original_price = game.find(class_="discount_original_price").text
            price = game.find(class_="discount_final_price").text

            data.append({
                "title": title,
                "original_price": original_price,
                "discount": discount,
                "price": price
            })
        except Exception as e:
            print("Error:", e)
            continue

    return data