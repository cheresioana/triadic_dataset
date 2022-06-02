import pandas as pd

if __name__ == '__main__':
    ds = pd.read_csv('data_spotify.csv', index_col=0)
    print(ds.head())
    print(ds.columns)

    #Define 2 conditions based on which to generate the triadic : chill and energy
    #For the chill define conditions:  acousticness > 0.5; danceability < 0.6; energy < 0.5; instrumentalness > 0.5
    df_chill = ds[(ds['acousticness'] >0.5) & (ds['danceability'] <0.6) & (ds['energy'] <0.5) & (ds['instrumentalness'] > 0.5)]

    #For the energy also define condition: acousticness < 0.8; danceability > 0.4; energy > 0.3; instrumentalness < 0.8
    df_energy = ds[(ds['acousticness'] < 0.8) & (ds['danceability'] > 0.4) & (ds['energy'] > 0.3) & (ds['instrumentalness'] < 0.8)]
    print(df_chill.head())
    print(df_energy.head())

    '''
    Write data to file according to the format required by fca tools bundle
    obj_name,attribute,condition
    
    Note: the name of the song is not written because it fails at upload due to weird characters
    '''

    f = open("triadic_dataset.csv", "w")
    for index, row in df_chill.iterrows():
        #song_title = row['song_title'].replace(',', '')
        song_title = 'song_'+str(index)
        try:
            s = '{0},acousticness,chill_music\n'.format(song_title)
            f.write(s)
            s = '{0},instrumentalness,chill_music\n'.format(song_title)
            f.write(s)
            if row['danceability'] >= 0.5:
                s = '{0},danceability,chill_music\n'.format(song_title)
                f.write(s)
        except:
            print(row['song_title'] + ' entry could not be added ')

    for index, row in df_energy.iterrows():
        #song_title = row['song_title'].replace(',', '')
        song_title = 'song_' + str(index)
        try:
            s = '{0},danceability,energy_music\n'.format(song_title)
            f.write(s)
            s = '{0},energy,energy_music\n'.format(song_title)
            f.write(s)
            if row['instrumentalness'] >= 0.5:
                f.write('{},instrumentalness,energy_music\n'.format(song_title))
        except:
            print(row['song_title'] + ' entry could not be added ')
    f.close()


