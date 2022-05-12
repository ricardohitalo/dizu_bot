from mechanize import Browser
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from time import sleep

from sympy import true
from credenciais import pwd, dizu, insta_user, insta_pwd
# =====================================================

class bot():

    def __init__(self, dizu, pwd):

        self.dizu = dizu
        self.pwd = pwd
        # self.conta = conta

        # browser = Chrome()
        self.options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self.browser = webdriver.Chrome()

    def dizu_login(self):
        self.browser.implicitly_wait(10)
        self.browser.get('https://painel.dizu.com.br/login')

        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'login').send_keys(self.dizu)
        
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'senha').send_keys(self.pwd)

        sleep(2)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        sleep(5)

    def insta_login(self, user, pwd):
        self.browser.implicitly_wait(10)
        self.browser.get('https://instagram.com')
        
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.NAME, 'username').send_keys(user)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.NAME, 'password').send_keys(pwd)
        
        sleep(2)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        sleep(5)

    def dizu_instagram_tasks(self, conta):
        self.browser.get('https://painel.dizu.com.br/painel/conectar')
        
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'instagram-tab').click()

        #* Selecionando conta para fazer a tarefa

        self.browser.implicitly_wait(10)
        select = Select(self.browser.find_element(By.ID, 'instagram_id'))
        select.select_by_visible_text(conta + '(Instagram)')
        # self.browser.find_element_by_id('iniciarTarefas').click()

        #* Start task

        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'iniciarTarefas').click()

        #* Start instagram follow task

        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, 'conectar_step_4').click()
        sleep(5)

        #* Change dizu_tab for instagram_tab

        alltabs = self.browser.window_handles
        self.browser.switch_to.window(alltabs[1])

        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//*[contains(text(), 'Seguir')]").click()
        sleep(3)

        if ( bool(self.browser.find_element(By.XPATH, "//*[contains(text(), 'Enviar mensagem')]")) == True ):
            print('Seguindo conta')
        
        self.browser.close()
        self.browser.switch_to.window(alltabs[0])

        self.browser.find_element(By.ID, 'conectar_step_5').click()


for i in range(len(insta_user)):
    init = bot(dizu, pwd)
    init.insta_login(insta_user[i], insta_pwd[i])
    init.dizu_login()
    init.dizu_instagram_tasks(insta_user[i])
