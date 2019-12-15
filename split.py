## Splitting the collected data: take only movies of a certain genre, pull out character names, guess gender, and assign dialogue.
import csv
import gender_guesser.detector as gender

d = gender.Detector(case_sensitive = False)
long_path = './data/'

def gather_genre(g):
    '''Gather the titles of movies of a certain genre
        input: g (desired genre, string)
        output: titles (movie titles, list of strings)'''

    f = open(long_path+'successful_files.csv', 'r')
    reader = csv.reader(f, delimiter=';')
    titles = []
    # print(reader)
    for row in reader:
        # print('Row!')
        if g in row[1]:
            # print('Genre!')
            titles.append(row[3])
    return titles

def gather_characters(titles):
    '''Access the files for those titles and pull out their characters by name, gather all info.
        input: titles (desired titles, list of strings)
        output: charas (character info, dictionary)'''

    charas = {}
    for t in titles:
        f = open(long_path + 'texts/' + t + '.txt')
        txt = f.read()
        pars = txt.split("\n")
        for i in range(len(pars)):
            par = pars[i]
            check = par.split(' ')
            if len(check) == 1 and check[0].isupper():
                name = check[0].strip()
                name = name.strip(':;,.?!()')
                g = d.get_gender(name)
                if g != 'unknown':
                    dialo = pars[i+1].replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!', '').replace(':', '').replace('-', '').replace('\t', '').replace('\n', '').replace('(', '').replace(')', '')
                    if g == 'mostly_male':
                        g = 'male'
                    elif g == 'mostly_female':
                        g = 'female'
                    if name in charas:
                        s = charas[name][1] + " " + dialo
                        charas[name] = [g, s]
                    else:
                        charas[name] = [g, dialo]
    return charas

def to_file(g, dic):
    '''Save data from dictionary to a file for easier retrieval later.
        input: g (desired genre, string), dic (character info, dictionary)
        output: none'''

    f = open(long_path + g + "_data.csv", 'w')
    for key in dic:
        l = [key, dic[key][0], dic[key][1]]
        f.write(';'.join(l) + '\n')




if __name__ == '__main__':
    genre = 'Horror'
    titles = gather_genre(genre)
    charas = gather_characters(titles)
    to_file(genre, charas)
