##############################################################################
# Analysis Cell
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

class AnalysisCell():
    _param = None
    _bse = None
    _tvalue = None
    _pvalue = None
    
    def param(self, param):
        self._param = param
        
    def bse(self, bse):
        self._bse = bse
        
    def tvalue(self, tvalue):
        self._tvalue = tvalue
        
    def pvalue(self, pvalue):
        self._pvalue = pvalue
        
    def _write(self, ws, row, col, format):
        text = '{:.3f} \n ({:.3f}) \n t = {:.2f}, p = {:.3f}'.format(
            self._param, self._bse, self._tvalue, self._pvalue)
        ws.write(row, col, text, format)
        