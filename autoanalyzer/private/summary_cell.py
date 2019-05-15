##############################################################################
# Summary Cell
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

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
        text = '{:.2f} \n ({:.2f}) \n'.format(self._mean, self._std)
            
        if self._pctiles is not None:
            for pctile, val in self._pctiles:
                text += 'p{} = {:.2f} \n'.format(pctile, val)
        else:
            for val, freq in self._freq:
                text += '{}: {:.2f} \n'.format(val, freq)
                
        text += 'N={}'.format(self._N)

        ws.write(row, col, text, format)