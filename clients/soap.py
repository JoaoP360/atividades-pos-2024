import zeep
from xml.dom.minidom import parseString

wsdl_countries = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
wsdl_number_to_words = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

countries_client = zeep.Client(wsdl=wsdl_countries)
numbers_client = zeep.Client(wsdl=wsdl_number_to_words)

def parse_soap_response(raw_response):
    """Parse e imprime uma resposta SOAP em formato legível."""
    parsed_xml = parseString(raw_response)
    print(parsed_xml.toprettyxml())

def get_capital(country_code):
    """Obtém a capital do país usando o código ISO."""
    print(f"Obtendo a capital do país com código {country_code}...")
    capital = countries_client.service.CapitalCity(sCountryISOCode=country_code)
    print(f"A capital do país ({country_code}) é: {capital}")

def number_to_words(number):
    """Converte um número em palavras (em inglês)."""
    print(f"Convertendo o número {number} para palavras em inglês...")
    words = numbers_client.service.NumberToWords(ubiNum=number)
    print(f"O número {number} por extenso é: {words}")

while True:
    print("\n" + "=" * 10 + " SOAP CLIENT " + "=" * 10 + "\n")
    print("1. Qual a capital da Noruega? ")
    print("2. Número por Extenso (em Inglês)")
    print("0. Encerrar")
    option = input("\nEscolha uma opção: ")
    print("")

    if option == "0":
        print("Encerrando o programa...")
        break

    elif option == "1":
        print("=" * 10 + " CAPITAL DA NORUEGA " + "=" * 10)
        get_capital("NO")

    elif option == "2":
        print("=" * 10 + " NÚMERO POR EXTENSO " + "=" * 10)
        try:
            number = int(input("Digite um número: "))
            number_to_words(number)
        except ValueError:
            print("Por favor, insira um número válido.")

    else:
        print("Opção inválida! Tente novamente.")
