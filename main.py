import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# List of user-agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0"
]

# Randomly select a user-agent and window size
selected_user_agent = random.choice(user_agents)
window_sizes = [(1920, 1080), (1280, 800), (1440, 900)]
selected_window_size = random.choice(window_sizes)

# Create an Options object and set the user agent
options = Options()
options.add_argument(f"user-agent={selected_user_agent}")
options.add_argument(f"--window-size={selected_window_size[0]},{selected_window_size[1]}")
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--headless")  # Uncomment to run in headless mode

# Path to webdriver
driver_path = r'C:\Automation\chromedriver.exe'
service = Service(driver_path)

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

store=set()
def get_link():
    url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaKcBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuALL18u0BsACAdICJDRjMzQ4Nzk0LTM5NmEtNDI4OS04Mzk2LWQ4ODZkZDNjNTdkZdgCBeACAQ&aid=304142&ss=Abuja&ssne=Abuja&ssne_untouched=Abuja&lang=en-us&src=index&dest_id=-1997013&dest_type=city&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204"

    driver.get(url)
    for _ in range(2):  # Adjust the number of scrolls as needed
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(3) 
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"b9687b0063"))
    )
    time.sleep(random.uniform(1.0, 3.0))  # Introduce a random delay
    # show=driver.find_element(By.CLASS_NAME,"bf33709ee1.a190bb5f27.dc0e35d124.a746857c37.e8d0e5d0c1.b81c794d25f0298d74a8")
    # if show:
    #     show.click()
    actions = ActionChains(driver)
    actions.move_by_offset(100, 200).perform() 
    for i in range(10):
        
        try:
            
            scroll_distance=2200
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            time.sleep(15)
            next=driver.find_element(By.CLASS_NAME,"dba1b3bddf.e99c25fd33.ea757ee64b.f1c8772a7d.ea220f5cdc.f870aa1234")
            if next:
                next.click()
                time.sleep(10)
            
            sub_element =element.find_elements(By.CLASS_NAME,"c655c9a144")
            for i in sub_element:
                title=i.find_element(By.CLASS_NAME,"f0ebe87f68").get_attribute('href')
                store.add(title)
            print(len(store))
        
        
        
        except Exception as e:
        
            print(f"Error extracting sub-element: {str(e)}")

    return store
data=[]

def get_page(link_to_pages):

    try:

        for link in link_to_pages:
            url_2=link
            driver.get(url_2)
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(3) 
            page=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"basiclayout"))
            )
            hotel_name=page.find_element(By.ID,"hp_hotel_name_reviews").text
            address=page.find_element(By.CLASS_NAME,"hp_address_subtitle.js-hp_address_subtitle.jq_tooltip").text
            packages=[]
            elements = driver.find_elements(By.CLASS_NAME, "e2585683de.fcfa97735d")
            for element in elements[:5]:  # Loop through the first 5 elements
                text = element.text
                packages.append(text)
            

            temp={
                "hotel_name":hotel_name,
                "address":address,
                "packages":packages,
                "link":url_2

            }

            data.append(temp)

    except Exception as e:
        print(f"Error extracting sub-element: {str(e)}")
    return data

link_to_pages=get_link() 
print(get_page(link_to_pages))




# except Exception as e:
#     print(f"Error occurred: {str(e)}")

# finally:
#     driver.quit()