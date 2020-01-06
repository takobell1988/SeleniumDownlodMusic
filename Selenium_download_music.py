from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def download_soundcloudmp3():
    contents = open('urls.txt', "r")

    urls = contents.readlines()
    for line in urls:
        try:
            print("trying to download " + line, end='')
            Chrome_driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')
            Chrome_driver.get('https://soundcloudmp3.cc/')
            Chrome_driver.find_element_by_id("videoURL").send_keys(str(line))
            Chrome_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/select/optgroup/option[3]').click()
            sleep(2)
            Chrome_driver.find_element_by_name("submitForm").click()
            sleep(80)
            Chrome_driver.find_element_by_xpath('//*[@id="conversionSuccess"]/p[4]/a').click()
            sleep(80)
            print("success downloading : " + str(line))
            Chrome_driver.close()
        except BaseException as e:
            print(e.args)
            print("could not download : " + str(line))
            Chrome_driver.close()
    else:
        contents.close()
        print("Finish !")


# download_soundcloudmp3()


def download_klickaud():
    contents = open('urls.txt', "r")

    urls = contents.readlines()
    for line in urls:
        try:
            print("trying to download " + line, end='')
            Chrome_driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')
            Chrome_driver.get("https://www.klickaud.net/")
            sleep(5)
            Chrome_driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/form/input[1]').send_keys(str(line))
            sleep(5)
            Chrome_driver.find_element_by_id('dlMP3').click()
            sleep(8)
            print("success downloading : " + str(line))
            Chrome_driver.close()
        except BaseException as e:
            print("could not download : " + str(line))
            print(e.args)
            Chrome_driver.close()
    else:
        contents.close()
        print("Finish !")


download_klickaud()