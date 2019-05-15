##############################################################################
# Writer Base
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

POOLED_VAL = '---'

class WriterBase():
    # Write a title
    def _write_title(
            self, row_start, col_start, row_end, col_end, title, format):
            
        if row_start == row_end and col_start == col_end:
            self._ws.write(row_start, col_start, title, format)
            return
        self._ws.merge_range(
            row_start, col_start, row_end, col_end, title, format)