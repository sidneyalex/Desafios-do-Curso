#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
city = input('Digite o nome da cidade: ').strip()
city = city.upper()
print('A cidade começa com Santo no nome? {}'.format(city[:5] == 'SANTO'))
