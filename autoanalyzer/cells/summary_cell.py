##############################################################################
# Summary Cell
# by Dillon Bowen
# last modified 05/23/2019
##############################################################################

'''
Data:
    N: number of observations
    mean
    std: standard deviation
    pctiles: [(pctile, val)]
    freq: [(val, freq)]
'''
class SummaryCell():
    _N = None
    _mean = None
    _std = None
    _pctiles = None
    _freq = None
    
    def N(self, N):
        self._N = N
        
    def mean(self, mean):
        self._mean = mean
        
    def std(self, std):
        self._std = std
        
    def pctiles(self, pctiles):
        self._pctiles = pctiles
        
    def freq(self, freq):
        self._freq = freq
        
    def _write(self, ws, row, col, format):
        text = ''
        if self._mean is not None:
            text += '{:.2f} \n'.format(self._mean)
        if self._std is not None:
            text += '({:.2f}) \n'.format(self._std)
        if self._pctiles is not None:
            for pctile, val in self._pctiles:
                text += 'p{} = {:.2f} \n'.format(pctile, val)
        if self._freq is not None:
            for val, freq in self._freq:
                text += '{}: {:.2f} \n'.format(val, freq)
        if self._N is not None:
            text += 'N={}'.format(self._N)

        ws.write(row, col, text, format)