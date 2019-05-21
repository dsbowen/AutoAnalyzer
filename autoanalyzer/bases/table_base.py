##############################################################################
# Table Base
# by Dillon Bowen
# last modified 05/21/2019
##############################################################################

from autoanalyzer.data_frame import DataFrame
from autoanalyzer.bases.base import Base
import pandas as pd

class TableBase(Base):
    # Set writer
    def writer(self, writer=None):
        self._parent(
            new_parent=writer, parent_attr='_writer', child_attr='_tables')
            
    # Get writer
    def get_writer(self):
        return self._writer

    # Set the worksheet title
    def worksheet(self, worksheet='Main'):
        self._ws_title = worksheet
        
    # Get worksheet title
    def get_worksheet(self):
        return self._ws_title
        
    # Set DataFrame
    def df(self, df=DataFrame()):
        self._df = df
        
    # Get DataFrame
    def get_df(self):
        return self._df
        
    # Set vertical group variables
    # {vertical group variable: [group value]}
    def vgroups(self, vgroups=[]):
        self._vgroups = {v: [] for v in self._groups(vgroups)}
        
    # Get list of vertical group variables
    def get_vgroups(self):
        return list(self._vgroups)
        
    # Convert single group as string to list
    def _groups(self, groups):
        if type(groups) == str:
            return [groups]
        return groups
        
    # Get a series split on group variable and values of that series
    def _get_series_values(self, group):
        if self._df._vars[group]['type'] == 'numeric':
            series = pd.qcut(
                self._df[group], self._df._vars[group]['group_pctile'])
        else:
            series = self._df[group]
        return (series, series.unique())
        
    # Add constant to DataFrame and decorate
    def _decorate(self):
        if '_const' not in self._df:
            self._df['_const'] = 1
            self._df.labels({'_const':'Constant'})
        self._df.decorate()
