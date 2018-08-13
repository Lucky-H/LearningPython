#! python

"""
@author: "Lucky-H"
@file: make_db_pickle_recs
@date: 2018-08-05
@time: 16:07:59
"""


from initdata import bob, sue, tom
import pickle
for (key, value) in [('bob', bob), ('sue', sue), ('tom', tom)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(value, recfile)
    recfile.close()
