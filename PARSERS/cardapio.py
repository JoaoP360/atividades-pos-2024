from xml.dom.minidom import parcers 

dom = xml.dom.minidom.parcers ("cardapio.xml")

#Elemento rais do xml (cardarpio)
cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')
for prato in pratos:
  for prato in cardapio:
        id = prato.getElementsByTagName('id')[0].firstChild.data
        nome = prato.getElementsByTagName('nome')[0].firstChild.data
        descricao = prato.getElementsByTagName('descricao')[0].firstChild.data
        ingredientes = prato.getElementsByTagName('ingredientes')[0].firstChild.data
        preco = prato.getElementsByTagName('preco')[0].firstChild.data
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.data
        tempo_preparo = prato.getElementsByTagName('tempo_preparo')[0].firstChild.data
