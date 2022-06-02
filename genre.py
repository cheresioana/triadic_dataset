import pandas as pd


def enter_record(index, attribute, row, f):
    song_title = 'song_' + str(index)
    s = song_title + ',' + attribute + "," + row['genre'] + "\n"
    f.write(s)


if __name__ == '__main__':
    ds = pd.read_csv('genres_v2.csv')
    print(ds.head())
    print(ds.columns)

    # Define 2 conditions based on which to generate the triadic : chill and energy
    # For the chill define conditions:  acousticness > 0.5; danceability < 0.6; energy < 0.5; instrumentalness > 0.5

    f = open("triadic_dataset_genre.csv", "w")
    for index, row in ds.iterrows():
        # song_title = row['song_title'].replace(',', '')


        try:
            if (row['danceability'] > 0.5):
                enter_record(index, 'danceability', row, f)
            if (row['energy'] > 0.5):
                enter_record(index, 'energy', row, f)
            if (row['acousticness'] > 0.5):
                enter_record(index, 'acousticness', row, f)
            if (row['speechiness'] > 0.5):
                enter_record(index, 'speechiness', row, f)
            if (row['instrumentalness'] > 0.5):
                enter_record(index, 'instrumentalness', row, f)
            if (row['liveness'] > 0.5):
                enter_record(index, 'liveness', row, f)
        except:
            print(row['song_title'] + ' entry could not be added ')
    f.close()
    '''
    Write data to file according to the format required by fca tools bundle
    obj_name,attribute,condition

    Note: the name of the song is not written because it fails at upload due to weird characters
    '''

    '''f = open("triadic_dataset.csv", "w")
    for index, row in df_chill.iterrows():
        # song_title = row['song_title'].replace(',', '')
        song_title = 'song_' + str(index)
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
        # song_title = row['song_title'].replace(',', '')
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
    f.close()'''


