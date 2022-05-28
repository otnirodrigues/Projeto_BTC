import requests
import json
import pygame
from pygame import *
from win10toast import ToastNotifier



class aplication():

    def __init__(self):
        
        self.api_btc()
        self.notify()
        self.criando_janela()
        self.setando_texto()   

    def api_btc(self):
        cotacao = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
        cotacao = cotacao.json()
        self.cotacao_btc = cotacao['BTCBRL']["bid"]
        self.date_cotacao = cotacao['BTCBRL']["create_date"]

    def notify(self):
        toaster = ToastNotifier()
        toaster.show_toast("Valor BTC",
                            self.cotacao_btc,
                            icon_path='btc_icon.png',
                            duration=30)

    def criando_janela(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Cotação Bitcoin')  
        self.img = pygame.image.load('btc_icon.png')
        pygame.display.set_icon(self.img)  
    
    def setando_texto(self):
       while True:
            
            font = pygame.font.SysFont("comicsansms", 30)
            text = font.render("Valor BTC: {}".format(self.cotacao_btc), True, (255, 0, 0))  
            date = font.render("Data: {}".format(self.date_cotacao), True, (255, 0, 0)) 
            texto_pos = (200 - text.get_width() // 2, 100 - text.get_height() // 2)
            date_pos = (200 - date.get_width()// 2, 200 - date.get_height() // 2)
            self.screen.blit(text, texto_pos)
            self.screen.blit(date, date_pos)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            
            pygame.display.flip()
            pygame.display.update()

aplication()
