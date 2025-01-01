from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")  # Add headless option
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Increase page load timeout
driver.set_page_load_timeout(120)

# List to store the scraped data
data = []

# Function to load a page with retries
def load_page_with_retry(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            driver.get(url)
            return  # Exit the function if successful
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise Exception("Failed to load the page after multiple attempts")

# Function to scrape reviews and ratings from a product's review page
def scrape_reviews(product_url):
    load_page_with_retry(product_url)
    
    while True:
        try:
            # Wait for the reviews section to load
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item")))
            
            # Extract review and rating elements
            review_items = driver.find_elements(By.CSS_SELECTOR, ".item")
            for item in review_items:
                # Extract rating by counting the number of stars
                stars = item.find_elements(By.CSS_SELECTOR, ".container-star .star")

                for star in stars:
                    image = star.get_attribute("src")
                    print(image)

                rating = len(stars)
                
                # Extract review text
                try:
                    review_text = item.find_element(By.CSS_SELECTOR, ".item-content .content").text.strip()
                except Exception:
                    review_text = "No review text available"
                
                # Append the data
                data.append({"Review": review_text, "Rating": rating})
            
            # Handle pagination
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, ".next-button")
                if next_button.is_enabled():
                    next_button.click()
                    WebDriverWait(driver, 30).until(EC.staleness_of(next_button))  # Wait for page to refresh
                else:
                    break
            except Exception:
                print("No more pages.")
                break
        except Exception as e:
            print(f"Error during scraping: {e}")
            break

product_urls = [
    "https://www.daraz.com.np/products/meetion-mt-m360-usb-wired-optical-mouse-black-i128428161-s1035903538.html",
    "https://www.daraz.com.np/products/winter-thick-inside-fur-fake-skin-transparent-high-waist-stretchy-leggings-stockings-for-women-i129051210-s1037047210.html",
    "https://www.daraz.com.np/products/electric-hot-water-bag-with-fur-hand-pocket-i103420211-s1024126158.html",
    "https://www.daraz.com.np/products/stylish-trending-printed-double-sided-premium-shawl-winter-scarf-for-women-i129162051-s1037174434.html",
    "https://www.daraz.com.np/products/air-force-1-full-white-premium-sneaker-for-men-i128948194-s1036883805.html",
    "https://www.daraz.com.np/products/anarkali-gaun-dupatta-plazo-i133678750-s1055231038.html",
    "https://www.daraz.com.np/products/true-wireless-bluetooth-airpods-charging-case-super-sound-premium-wts-pro-2-i143339976-s1087190217.html"
]

for product_url in product_urls:
    print(f"Scraping reviews for: {product_url}")
    scrape_reviews(product_url)

df = pd.DataFrame(data)
df.to_csv("daraz_reviews.csv", index=False)

driver.quit()

print("Scraping completed. Data saved to 'daraz_reviews.csv'.")
