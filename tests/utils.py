import re
import pytest
from playwright.sync_api import Page, expect, Browser

def login_pipeline(page):
     # Comando goto usado para ir para o endereço desejado
    page.goto("http://localhost:3000/")
    
    # Fechar mensagem de boas vindas
    page.locator(".close-dialog").click()
    
    # Navegar para a tela de login
    page.locator("#navbarAccount").click()
    page.locator("#navbarLoginButton").click()
    
    page.locator("#email").fill("admin@juice-sh.op")
    page.locator("#password").fill("admin123")
    
    page.locator("#loginButton").click()