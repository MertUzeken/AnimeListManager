# Author: Mert Uzeken
# Project Name: Anime List Manager

from pandas import *

class Loader():
    def __init__(self):
        self.titleReader()

    def titleReader(self):
        file_name = 'completed.xlsx'
        df = read_excel(file_name,header=None)
        self.titles_list = ()
        self.titles_list = df.values.tolist()
        return self.titles_list

Loader()