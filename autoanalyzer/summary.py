##############################################################################
# Summary Block
# by Dillon Bowen
# last modified 05/14/2019
##############################################################################

from autoanalyzer.private.writer_base import WriterBase
import xlsxwriter

class Summary(WriterBase):
    def __init__(self, table=None, vars=[], title='Summary Statistics'):
        self.table(table)
        self.title(title)
        self.vars(vars)
        self._cells = {}
        
    # Set the Table or TableGenerator to which this summary block belongs
    def table(self, table=None):
        try:
            self._table.remove(self)
        except:
            pass
        if table is not None:
            table._blocks.append(self)
        self._table = table
        
    # Set block title
    def title(self, title='Summary Statistics'):
        self._title = title
        
    # Set the summary variables
    def vars(self, vars=[]):
        self._vars = vars
        self._ncols = len(vars)
    
    
    
    ###########################################################################
    # Generate summary statistics
    ###########################################################################
    
    # Generate summary statistics cells
    # must be assigned to a table
    # cells: {vgroup: {vgroup_val: {var: data}}}
    def generate(self):
        vgroup, vgroup_val = self._table._vgroup, self._table._vgroup_val
        if vgroup not in self._cells:
            self._cells[vgroup] = {}
        self._cells[vgroup][vgroup_val] = {v: 'data' for v in self._vars}
        
    def _generate_by_vgroup(self, vgroup):
        print(vgroup)
        self._cells[vgroup] = {v: {} for v in self._table._vgroups[vgroup]}
        print('summary', self._table._vgroups)
        [self._generate_by_vgroup_val(self._cells[vgroup], val)
            for val in self._table._vgroups[vgroup]]
            
    def _generate_by_vgroup_val(self, vgroup_dict, vgroup_val):
        vgroup_dict[vgroup_val] = {var: 'data' for var in self._vars}
        # cell has vgroup, vgroup_val, data
        # data is a list of rows in cell
        # cells[vgroup][vgroup_val][var] = data
        
    
    
    ###########################################################################
    # Write to table
    ###########################################################################
    
    # Write
    # write title
    # write heading
    # write data (cells)
    def _write(self, row, col, ws, head_format, cell_format):
        self._ws = ws
        self._write_title(
            row, col, row, col+self._ncols-1, self._title, head_format)
        [ws.write(row+1, col+i, self._table._vars[v]['label'], head_format)
            for i,v in enumerate(self._vars)]
        
    