#!/usr/bin/python
# encoding: utf-8

''' ####################################################################################### ''

Script em Python para reiniciar o Modem/Roteador Powerbox GVT SAGEMCOM FAST2764_v8480

''' ####################################################################################### ''

__author__ = "Eduardo Quintanilha"
__email__ = "quintanilhaedu@gmail.com"
__version__ = "1.0.0"

# Início: 30/01/2017 19:20h
# Funcionando: 30/01/2017 23:04h (Ainda fiz a janta rsrs)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys

global user, pwd

user = 'admin'
pwd = 'gvt12345'

#------ Navegador na web e Login na página com Firefox --------#
def Login():
	url = "http://{}:{}@192.168.25.1/index.cgi".format(user,pwd)
	try:
		driver = webdriver.Firefox()
	except:
		sys.exit('Erro ao obter o Navegador Firefox!\nSaindo...\n')
	try:
		driver.get(url)
	except:
		sys.exit('Erro ao obter a url da página!\nSaindo...\n')
	time.sleep(2)
	driver.switch_to_alert().accept()
	print('Login efetuado com sucesso!\n')
	return(driver)
#---------------------------------------------------------------#

#------ Abre os links até chegar na página de reboot -----------#
def RebootPage():
	driver = Login()
	gerenc = 'Gerenciamento'
	reset = 'Resets'
	reboot = 'Reiniciar'

	# Abre link 'Gerenciamento'
	try:
		time.sleep(5)
		link_gerenc = driver.find_element_by_link_text(gerenc)
	except:
		print('Erro ao obter link "{}".\nTentando novamente...\n'.format(gerenc))
		time.sleep(3)
		link_gerenc = driver.find_element_by_link_text(gerenc)
	link_gerenc.click()

	# Abre link 'Resets'
	try:
		time.sleep(5)
		link_reset = driver.find_element_by_link_text(reset)
	except:
		print('Erro ao obter link "{}".\nTentando novamente...\n'.format(reset))
		time.sleep(3)
		link_reset = driver.find_element_by_link_text(reset)	
	link_reset.click()
	return(driver)
#-----------------------------------------------------------------------#

#----------------- Executa Reboot ---------------------------------#
def RebootRun():
	reboot = 'Reiniciar'
	driver = RebootPage()

	try:
		time.sleep(3)
		btn_reboot = driver.find_element_by_link_text(reboot)
		btn_reboot.click()
	except:
		print('Erro ao clicar no botão "{}"\n'.format(reboot))

	try:
		time.sleep(2)
		btn_sim = driver.find_element_by_id('jqi_state0_buttonSim')
		time.sleep(2)
		btn_sim.click()
		time.sleep(2)
	except:
		print('Erro ao clicar no botão de sim!\n')

	sys.exit('Roteador reiniciado com sucesso!\nSaindo...\n\n')
#--------------------------------------------------------------------------#




if __name__ == '__main__':
	RebootRun()

