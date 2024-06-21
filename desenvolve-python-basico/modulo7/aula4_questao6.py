import csv

def deve_ignorar_linha(artist_name):
    return artist_name.startswith('"') and artist_name.endswith('"')

musicas_populares = []

# Abre o arquivo CSV
with open('spotify-2023.csv', mode='r', encoding='latin-1') as arquivo_csv:
    csv_reader = csv.reader(arquivo_csv)
    
    next(csv_reader)
    
    musica_por_ano = {}

    for linha in csv_reader:
        track_name = linha[0].strip()
        artist_name = linha[1].strip()
        artist_count = int(linha[2].strip())
        released_year = int(linha[3].strip())
        streams = int(linha[8].strip())

        if deve_ignorar_linha(artist_name):
            continue
        
        if released_year >= 2012 and released_year <= 2022:
            if released_year not in musica_por_ano:
                musica_por_ano[released_year] = [track_name, artist_name, released_year, streams]
            else:
                if streams > musica_por_ano[released_year][3]:
                    musica_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    musicas_populares = list(musica_por_ano.values())

musicas_populares.sort(key=lambda x: x[2])

for musica in musicas_populares:
    print(musica)