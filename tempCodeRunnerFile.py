# Scrape the NASA Web Page
# and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.

def init_browser():
    executable_path = {"executable_path": "mission_to_mars\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # Visit https://mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the article title 
    article_title = soup.find('div', id='content_title').text

    # Get the article paragraph
    article_teaser = soup.find('div', id='article_teaser_body').text
    
    
    # Store data in a dictionary
    article_data = {
        "news_title": article_title,
        "news_teaser": article_teaser
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return article_data
