from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from flags import kullanici_adi, sifre



# İnstagrama Giriş
tarayici = webdriver.Chrome(ChromeDriverManager().install())
tarayici.maximize_window()
tarayici.get("https://www.instagram.com/")
sleep(3)

tarayici.find_element(By.NAME, "username").click()
tarayici.find_element(By.NAME, "username").send_keys(kullanici_adi)

tarayici.find_element(By.NAME, "password").click()
tarayici.find_element(By.NAME, "password").send_keys(sifre)

sleep(2)

login_path = '//*[@id="loginForm"]/div/div[3]'

tarayici.find_element(By.XPATH,login_path).click()

sleep(5)


# Profile sayfasına ulaşıldı.
profile_image = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]'

tarayici.find_element(By.XPATH, profile_image).click()

sleep(3)


tarayici.find_element(By.CLASS_NAME, "-qQT3").click()
sleep(3)


# Takip edilenler butonuna
tarayici.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > main:nth-child(2) > div:nth-child(1) > header:nth-child(1) > section:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1) > div:nth-child(1').click()
sleep(3)

# Takip ettiğiniz hesaplardan seçtiğiniz bir tanesinin sayfsaına ulaşıldı.
tarayici.find_element(By.XPATH, "//span[contains(text(),'teknolojiaihl')]").click()
sleep(2)

# Ulaştığınız sayfadaki son göderiyi açar.
tarayici.find_element(By.XPATH, "(//div[@class='_aagw'])[1]").click()
sleep(2)

# Açılan gönderiyi beğenir
tarayici.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Beğen'])[2]").click()
sleep(3)

#Tarayıcıdan çıkar
tarayici.quit()