from xml.dom.minidom import parcers 

dom = xml.dom.minidom.parcers ("cardapio.xml")

#Elemento rais do xml (cardarpio)
cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')
for prato in pratos:
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue 
    descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue 
    ingredientes = prato.getElementsByTagName("ingrediente")
    ingredientes = [f"   - {ingrediente.firstChild.nodeValue}" for ingrediente in ingredientes] 

    preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue 
    calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue 
    tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue 

print("")
print("="*30)
print(f"Nome: {nome}")
print(f"Descrição: {descricao}")
print("Ingredientes:")
print("\n".join(ingredientes))
print(f"Preço: R$ {preco}")
print(f"Calorias: {calorias} kcal")
print(f"Tempo de preparo: {tempoPreparo}")
print("="*30)
