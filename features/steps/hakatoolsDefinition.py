from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class HakatoolsDefinition:
    
    @given(u'ingreso a la url "{url}"')
    def step_impl_ingresar_url(context, url):
        print("hola! esta funcionando")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("start-maximized")
        context.browser = webdriver.Chrome(executable_path=r"./driver/chromedriver.exe", options=options)
        context.browser.get(url)
        time.sleep(3)
        
    @when(u'hago click en la seccion formularios')
    def step_impl(context):
        context.browser.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        form_button = context.browser.find_element_by_id("cardGoForms")
        form_button.click()
        time.sleep(3)

    @then(u'valido que me encuentro en la seccion formularios')
    def step_impl(context):
        context.browser.execute_script("window.scrollTo(0, 0)")
        time.sleep(3)
        form_text = context.browser.find_element_by_xpath("//h1[text()='Formularios']")
        # if form_text.text == "Formularios":
        #     assert True
        # else:
        #     assert False
        assert form_text.text == "Formularios"