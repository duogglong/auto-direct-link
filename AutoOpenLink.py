from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

for _ in range(10000):
    driver.execute_script("window.open('https://www.highrevenuenetwork.com/x78bxx86u5?key=9ef290a5ce2d96c8367b7cf544c50ad2', '_blank');")
    # time.sleep(1)  # Đợi một giây giữa các lần mở tab để đảm bảo tất cả các tab đều được mở đúng cách
    driver.switch_to.window(driver.window_handles[-1])  # Chuyển tới tab mới mở
    time.sleep(10)  # Đợi 10 giây
    driver.close()  # Đóng tab hiện tại
    driver.switch_to.window(driver.window_handles[0])  # Quay lại tab đầu tiên

# Đợi 12 giây để tất cả các tab tải nội dung
time.sleep(12)

# Đóng trình duyệt sau khi hoàn thành
driver.quit()
