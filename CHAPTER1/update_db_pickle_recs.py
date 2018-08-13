#! python

"""
@author: "Lucky-H"
@file: update_db_pickle_recs
@date: 2018-08-05
@time: 20:19:53
"""


import pickle
suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10

suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()