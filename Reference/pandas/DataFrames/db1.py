# Fazendo a junção de dois DataFrames
import pandas as pd
from db import DemoDB

dtab = DemoDB()

# Será feita a junção de dois DataFrames, para que a informação de um complemente a outra
album = dtab.tables.Album.all()
artist = dtab.tables.Artist.all()

# DataFrames salvos
# print(album.head())
# print(artist.head())

# Unindo os DataFrames
# album_artist = pd.merge(artist, album)

# Essa união ocorre porque nos dois datasets as tabelas são iguais
album.rename(columns ={ 'ArtistId': 'Artist_Id'}, inplace = True)

# Veja que o merge não irá funcionar
# album_artist = pd.merge(artist, album)

# Para resolver este problema basta especificar o que cada elemento tem de diferente
# Isso faz o pandas entender que eles são iguais e junta-los
album_artist = pd.merge(album, artist, left_on= 'Artist_Id', right_on = 'ArtistId')

