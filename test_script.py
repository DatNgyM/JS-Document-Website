from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Đảm bảo đường dẫn đúng tới msedgedriver.exe trong thư mục Edge
edge_driver_path = 'C:/Users/DAT DAT/Documents/GitHub/JS-Document-Website/Edge/msedgedriver.exe'

# Cấu hình WebDriver cho Edge
service = Service(executable_path=edge_driver_path)
options = Options()
options.use_chromium = True  # Edge sử dụng Chromium engine

# Khởi tạo driver
driver = webdriver.Edge(service=service, options=options)

# Truy cập vào trang web của bạn
driver.get("file:///C:/Users/DAT DAT/Documents/GitHub/JS-Document-Website/index.html")  # Đảm bảo đường dẫn đúng

# 1. Kiểm tra chức năng tìm kiếm và tô sáng từ khóa
search_input = driver.find_element(By.ID, 'search-bar')
search_input.send_keys('JavaScript')  # Tìm kiếm từ khóa "JavaScript"
time.sleep(2)  # Đợi một chút

# Kiểm tra số lượng từ khóa được tô sáng
highlighted_elements = driver.find_elements(By.CLASS_NAME, 'highlight')
print(f"Số lượng từ khóa được tô sáng: {len(highlighted_elements)}")

# 2. Kiểm tra các liên kết trong navbar (các thẻ <a> với href dẫn đến các phần trong trang)
links = driver.find_elements(By.CSS_SELECTOR, '#navbar a')

for link in links:
    # Đảm bảo phần tử có thể click được trước khi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(link)
    )
    
    # Cuộn tới phần tử để đảm bảo nó hiển thị
    actions = ActionChains(driver)
    actions.move_to_element(link).perform()
    time.sleep(1)  # Đợi để đảm bảo phần tử đã ở trong view

    # Click vào liên kết bằng JavaScript nếu cần thiết
    driver.execute_script("arguments[0].click();", link)
    time.sleep(1)  # Đợi trang cuộn đến phần tương ứng
    print(f"Đã chuyển đến phần: {link.get_attribute('href')}")

# Đóng trình duyệt sau khi kiểm thử xong
driver.quit()
