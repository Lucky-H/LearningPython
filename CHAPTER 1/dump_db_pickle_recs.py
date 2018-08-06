#! python

"""
@author: "Lucky-H"
@file: dump_db_pickle_recs
@date: 2018-08-05
@time: 16:19:35
"""


import pickle
import  glob

for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    recode = pickle.load(recfile)
    recfile.close()
    print(filename, '=>\n', recode)

suefile = open('sue.pkl', 'rb')
print('sue => ', pickle.load(suefile)['pay'])
suefile.close()
