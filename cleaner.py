__author__ = 'Liam'from collections import Counterclass Cleaner(object):    def __init__(self, csv_data):        self.change_misc_values(csv_data)        self.clean_data, self.empty_columns = self.remove_empty_columns(            csv_data)    @staticmethod    def change_misc_values(csv_data):        """        Replaces identified values of unclear meaning or inexact value        , i.e., '-', with an agreed value.        :return:        """        for i in csv_data:            for index, item in enumerate(i[1]):                if item == '-':                    i[1][index] = ''    @staticmethod    def remove_empty_columns(csv_data):        clean_data = []        empty_columns = []        for i in csv_data:            if Counter(i[1]).most_common(1)[0][0] == '':                if Counter(i[1]).most_common(1)[0][1] / len(i[1]) >= .9:                    empty_columns.append(i)            else:                clean_data.append(i)        return clean_data, empty_columns