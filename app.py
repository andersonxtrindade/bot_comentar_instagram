from selenium import webdriver
from time import sleep
from random import randint, choice

class ChromeAuto:
    def __init__(self):
        self.caminho = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.caminho,
            options=self.options
        )


    def digite_pessoa(self, frase):
        for letra in frase:
            onde_digitar = self.chrome.find_element_by_class_name('Ypffh')
            onde_digitar.send_keys(letra)
            sleep(randint(1, 5)/30)


    def clica_campo_comentario(self):
        try:
            campo_comentario = self.chrome.find_element_by_class_name('Ypffh')
            campo_comentario.click()
        except Exception as e:
            print('Erro ao clicar no campo do comentario', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def enviar(self):
        try:
             self.chrome.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
        except Exception as e:
            print('Erro ao enviar', e)


    def principal(self):
        comentarios = ['Já pensou ganhar, estouro', 'Salve familia, vai dar nois nessa fita', 'Bora que bora',
                       'Esse eu ganho', 'Só bora', 'Dale', 'Bora que bora']
        self.acessa('https://www.instagram.com/p/CEsQCkmjQhy/')
        sleep(2)
        ex = 0
        while ex == 0:
            sleep(randint(3, 7))
            self.digite_pessoa(choice(comentarios))
            sleep(3)
            self.enviar()
            sleep(randint(150, 300))


chrome = ChromeAuto()
chrome.principal()
