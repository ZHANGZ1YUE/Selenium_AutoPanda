import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



option = Options()
option.add_argument('user-data-dir=/Users/zhangziyue/Library/Application Support/Google/Chrome/')
driver = webdriver.Chrome(executable_path='/Users/zhangziyue/Desktop/chromedriver', options=option)
driver.get('https://cas.ecs.kyoto-u.ac.jp/cas/login?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer')


id_box = driver.find_element_by_name('username') #input id
id_box.send_keys('用户名')

pass_box = driver.find_element_by_name('password') #input password
pass_box.send_keys('密码')

login_button = driver.find_element_by_name('submit') #click on login
login_button.click()

more_button = driver.find_element_by_xpath('//*[@title="More Sites"]') #use this complicated shit to drag down more sites
more_button.click()

time.sleep(1)
#driver.implicitly_wait(3)  #不知道为什么有这一句，这一句不管在哪都可以正常加载下一个，即使不在这一行，在上面的话，下面选课这一行仍然能


#Choose which course you would like to autoclick
#course_box = driver.find_element_by_xpath('//*[@id="2020-110-3524-000"]')   #Public Economics
#course_box = driver.find_element_by_xpath('//*[@id="2020-110-3519-000"]')   #Soil Mechanics
course_box = driver.find_element_by_xpath('//*[@id="2020-110-3522-000"]')   #Fourier Adv Cal
course_box.click()


zoom_box = driver.find_element_by_xpath('//*[@title="For accessing an external website within the site."]')
zoom_box.click()


driver.switch_to.window(driver.window_handles[1])  ##Go to next page
driver.implicitly_wait(5) #time sleep不好掌握等多长时间，所以还是这个
#time.sleep(5)
#zoom_join = driver.find_element_by_xpath("//a[@class='ant-btn ant-table-span']") #Soil
zoom_join = driver.find_element_by_xpath("//tr[1]//td[4]//div[1]//div[1]//a[1]") #Fourier
zoom_join.click()

driver.switch_to.window(driver.window_handles[2]) #Next page
launch_meeting = driver.find_element_by_link_text("launch meeting")
launch_meeting.click()

#到这一步就做不下去了，这个弹窗我无法点出来
time.sleep(5)
obj = driver.switcht_to.alert()
obj.accept()
  #accpet the popup, note that it is no alert but a Dialog Box
