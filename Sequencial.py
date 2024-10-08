tam_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
vel_da_internet = float(input("Digite a velocidade da internet em Mbps:  "))
tempo_para_download = tam_arquivo/vel_da_internet
print(f"Vai demorar {tempo_para_download} segundos para baixar o arquivo!")
print("\nFim do programa!")