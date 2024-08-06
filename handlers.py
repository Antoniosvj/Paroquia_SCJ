from state import liturgia, oracoes, devocoes_carismas, calendario, contatos

def hide_all():
    liturgia.hide()
    oracoes.hide()
    devocoes_carismas.hide()
    calendario.hide()
    contatos.hide()

def show_liturgia(page):
    hide_all()
    liturgia.show()
    page.update()

def show_oracoes(page):
    hide_all()
    oracoes.show()
    page.update()

def show_devocoes_carismas(page):
    hide_all()
    devocoes_carismas.show()
    page.update()

def show_calendario(page):
    hide_all()
    calendario.show()
    page.update()

def show_contatos(page):
    hide_all()
    contatos.show()
    page.update()
