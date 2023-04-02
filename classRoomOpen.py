from subprocess import call
import pyautogui as pg
import time

# Lendo as credenciais no arquivo.txt
typeNav = open('navegadores.txt', 'r')
logLogin = open('login.txt', 'r')

nav = [iNav.strip() for iNav in typeNav]

login = [iCrend.strip() for iCrend in logLogin]
iSite = login[1]
iBrowser = login[4]
iEmail = login[7]
iPasswrd = login[10]

if iBrowser == "":
    iBrowser = "X"
else:
    pass

print(f'''
Navegador: {iBrowser}
{time.sleep(2)}
Site: {iSite:.28}
{time.sleep(2)}
Email: {iEmail}
{time.sleep(2)}
Senha: {iPasswrd}
''')

# Verificando as credenciais
if iBrowser == "" or iBrowser == "X":
    print("❗ - Verifique se o navegador está definido!")
    time.sleep(1)

else:
    print("✔ - Navegador: OK!")
    time.sleep(1)
if iSite == "":
    print("❗ - Verifique se o site está definido!")
    time.sleep(1)
else:
    print("✔ - Site: OK!")
    time.sleep(1)
if iEmail == "":
    print("❗ - Verifique se o email está definido!")
    time.sleep(1)
else:
    print("✔ - Email: OK!")
    time.sleep(1)
if iPasswrd == "":
    print("❗ - Verifique se o senha está definido!")
    time.sleep(1)
else:
    print("✔ - Senha: OK!")
    time.sleep(1)

# Abrindo navegador
if iBrowser == nav[0]:
    print("🟡 - Inicializando navegador...")
    time.sleep(1)
    call("\"C:\Program Files\Google\Chrome\Application\chrome.exe\" -incognito " + iSite, shell=False)
    print("🟢 - Navegador aberto!")
    time.sleep(1)
elif iBrowser == nav[1]:
    print("🟡 - Inicializando navegador...")
    time.sleep(1)
    call("\"C:\Program Files\Mozilla Firefox\\firefox.exe\" -private " + iSite, shell=False)
    print("🟢 - Navegador aberto!")
    time.sleep(1)
elif iBrowser == '':
    print("❗ - Defina um navegador")
    print("🔴 - Nenhum navegador encontrado!")
    while True:
        break
else:
    print("Aconteceu algo!")

for v in iBrowser:
    if v == '' or v == 'X':
        break
    else:
        time.sleep(20)
        # Preenchendo as crendenciais
        ## Preenchendo o campo de email.
        print("Colocando o email no campo")
        pg.write(iEmail)
        pg.press("enter")
        print("Email colocado")
        time.sleep(20)
        ## Preenchendo o campo de senha.
        print("Colocando a senha no campo")
        pg.write(iPasswrd)
        pg.press("enter")
        print("Senha colocada")

        # Finalizando
        print("Sucesso!!!")
        break