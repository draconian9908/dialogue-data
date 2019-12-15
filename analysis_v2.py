import csv
import operator
import nltk
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')

long_path = './data/'
f = open(long_path + "Horror_data.csv")
reader = csv.reader(f, delimiter=';')

data = {}#287 total names in Horror
training_set = {}
testing_set = {}
try_train = {}
try_test = {}
ac = 0
mc = 0
fc = 0

count = 0
for row in reader:
    if row[2] == '':
        dia = "silence"
    else:
        dialo = row[2].replace(',', '').replace('  ', ' ')
        spli = dialo.split()
        dia = ' '.join([i for i in spli if i.isalpha()])
    if row[1] == 'male':
        mc += 1
        ge = 0
    elif row[1] == 'female':
        fc += 1
        ge = 1
    elif row[1] == 'andy':
        ac += 1
        ge = 3
    if count < 5:
        try_train[row[0]] = [ge, dia]
    elif count < 10:
        try_test[row[0]] = [ge, dia]
    if count < 200:
        training_set[row[0]] = [ge, dia]
    else:
        testing_set[row[0]] = [ge, dia]
    count += 1
    data[row[0]] = [ge, dia]

f.close()

## Put everything into files. ##

def make_csv(p, d):
    f = open(p, 'w')
    for s in d:
        f.write(s + ", " + str(d[s][0]) + ", " + d[s][1] + "\n")
    f.close()

all_p = long_path + "Horror_all.csv"
try_test_p = long_path + "Horror_try_test.csv"
try_train_p = long_path + "Horror_try_train.csv"
test_p = long_path + "Horror_test.csv"
train_p = long_path + "Horror_train.csv"

make_csv(all_p, data)
make_csv(try_test_p, try_test)
make_csv(try_train_p, try_train)
make_csv(test_p, testing_set)
make_csv(train_p, training_set)

f = open(long_path + "Horror_g_count.txt", 'w')
f.write(str(mc) + "\n" + str(fc) + "\n" + str(ac))
f.close()
