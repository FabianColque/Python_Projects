
#writing in csv files

from csv import writer

#w - write
#a - increment

# with open('movies.csv', 'a') as myfile:
#     writer_csv = writer(myfile)
#     writer_csv.writerow(['Title', 'Genre', 'Duration'])
#     writer_csv.writerow(['Interstellar', 'Sci-Fi', '3h'])
#     writer_csv.writerow(['Time', 'Sci-Fi', '2h'])
#     writer_csv.writerow(['Chucky', 'Suspence', '2h'])
#     writer_csv.writerow(['Chucky2', 'Suspence', '2h'])


#DictWriter

from csv import DictWriter

with open('movies.csv', 'w') as myfile:
    header = ['Title', 'Genre', 'Duration']
    writer_csv = DictWriter(myfile, fieldnames=header)
    writer_csv.writeheader()
    movie = None
    while movie != 'exit':
        movie = input('Movie: ')
        if movie == 'exit':
            break
        genre = input('Genre: ')
        duration = input('Duration: ')
        writer_csv.writerow({'Title': movie, 'Genre': genre, 'Duration': duration})