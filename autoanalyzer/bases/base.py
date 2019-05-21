##############################################################################
# Base
# by Dillon Bowen
# last modified 05/21/2019
##############################################################################

class Base():
    # Assign self to parent
    # remove from old parent
    # assign to new parent
    def _parent(self, new_parent, parent_attr, child_attr):
        try:
            getattr(getattr(self, parent_attr), child_attr).remove(self)
        except:
            pass
            
        if new_parent is not None:
            getattr(new_parent, child_attr).append(self)
        setattr(self, parent_attr, new_parent)
        
    # Set title
    def title(self, title):
        self._title = title
        
    # Get title
    def get_title(self):
        return self._title