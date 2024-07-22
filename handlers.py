from state import liturgia, oracoes, devocoes_carismas, calendario, contatos

def show_liturgia(page):
    liturgia.visible = True
    oracoes.visible = False
    devocoes_carismas.visible = False
    calendario.visible = False
    contatos.visible = False
    page.update()

def show_oracoes(page):
    liturgia.visible = False
    oracoes.visible = True
    devocoes_carismas.visible = False
    calendario.visible = False
    contatos.visible = False
    page.update()

def show_devocoes_carismas(page):
    liturgia.visible = False
    oracoes.visible = False
    devocoes_carismas.visible = True
    calendario.visible = False
    contatos.visible = False
    page.update()

def show_calendario(page):
    liturgia.visible = False
    oracoes.visible = False
    devocoes_carismas.visible = False
    calendario.visible = True
    contatos.visible = False
    page.update()

def show_contatos(page):
    liturgia.visible = False
    oracoes.visible = False
    devocoes_carismas.visible = False
    calendario.visible = False
    contatos.visible = True
    page.update()
