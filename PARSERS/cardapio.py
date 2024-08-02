from xml.dom.minidom import parcers 

dom = xml.dom.minidom.parcers ("cardapio.xml")

#Elemento rais do xml (cardarpio)
cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')
for prato in pratos:
    element_nome = prato.getElementbyTagName('nome')[0]
    nome = element_nome.firstChild.nodeValue
    
    