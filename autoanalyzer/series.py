##############################################################################
# Series
# by Dillon Bowen
# last modified 05/23/2019
##############################################################################

from autoanalyzer.bases.frame_base import FrameBase
import pandas as pd

'''
Data:
    data: pandas Series
    vars: {var: {'label', 'type', 'group_pctiles', 'cell_pctiles'}}
'''
class Series(FrameBase):
    def T(self, *args, **kwargs):
        # print("T")
        return self._overload('T', *args, **kwargs)

    def _AXIS_ALIASES(self, *args, **kwargs):
        # print("_AXIS_ALIASES")
        return self._overload('_AXIS_ALIASES', *args, **kwargs)
    def _AXIS_IALIASES(self, *args, **kwargs):
        # print("_AXIS_IALIASES")
        return self._overload('_AXIS_IALIASES', *args, **kwargs)

    def _AXIS_LEN(self, *args, **kwargs):
        # print("_AXIS_LEN")
        return self._overload('_AXIS_LEN', *args, **kwargs)

    def _AXIS_NAMES(self, *args, **kwargs):
        # print("_AXIS_NAMES")
        return self._overload('_AXIS_NAMES', *args, **kwargs)

    def _AXIS_NUMBERS(self, *args, **kwargs):
        # print("_AXIS_NUMBERS")
        return self._overload('_AXIS_NUMBERS', *args, **kwargs)

    def _AXIS_ORDERS(self, *args, **kwargs):
        # print("_AXIS_ORDERS")
        return self._overload('_AXIS_ORDERS', *args, **kwargs)

    def _AXIS_REVERSED(self, *args, **kwargs):
        # print("_AXIS_REVERSED")
        return self._overload('_AXIS_REVERSED', *args, **kwargs)

    def _AXIS_SLICEMAP(self, *args, **kwargs):
        # print("_AXIS_SLICEMAP")
        return self._overload('_AXIS_SLICEMAP', *args, **kwargs)

    def __abs__(self, *args, **kwargs):
        # print("__abs__")
        return self._overload('__abs__', *args, **kwargs)

    def __add__(self, *args, **kwargs):
        # print("__add__")
        return self._overload('__add__', *args, **kwargs)

    def __and__(self, *args, **kwargs):
        # print("__and__")
        return self._overload('__and__', *args, **kwargs)

    def __array__(self, *args, **kwargs):
        # print("__array__")
        return self._overload('__array__', *args, **kwargs)

    def __array_prepare__(self, *args, **kwargs):
        # print("__array_prepare__")
        return self._overload('__array_prepare__', *args, **kwargs)

    def __array_priority__(self, *args, **kwargs):
        # print("__array_priority__")
        return self._overload('__array_priority__', *args, **kwargs)

    def __array_wrap__(self, *args, **kwargs):
        # print("__array_wrap__")
        return self._overload('__array_wrap__', *args, **kwargs)

    def __bool__(self, *args, **kwargs):
        # print("__bool__")
        return self._overload('__bool__', *args, **kwargs)

    def __bytes__(self, *args, **kwargs):
        # print("__bytes__")
        return self._overload('__bytes__', *args, **kwargs)

    def __class__(self, *args, **kwargs):
        # print("__class__")
        return self._overload('__class__', *args, **kwargs)

    def __contains__(self, *args, **kwargs):
        # print("__contains__")
        return self._overload('__contains__', *args, **kwargs)

    def __copy__(self, *args, **kwargs):
        # print("__copy__")
        return self._overload('__copy__', *args, **kwargs)

    def __deepcopy__(self, *args, **kwargs):
        # print("__deepcopy__")
        return self._overload('__deepcopy__', *args, **kwargs)

    def __delattr__(self, *args, **kwargs):
        # print("__delattr__")
        return self._overload('__delattr__', *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        # print("__delitem__")
        return self._overload('__delitem__', *args, **kwargs)

    def __dict__(self, *args, **kwargs):
        # print("__dict__")
        return self._overload('__dict__', *args, **kwargs)

    def __dir__(self, *args, **kwargs):
        # print("__dir__")
        return self._overload('__dir__', *args, **kwargs)

    def __div__(self, *args, **kwargs):
        # print("__div__")
        return self._overload('__div__', *args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        # print("__divmod__")
        return self._overload('__divmod__', *args, **kwargs)

    def __doc__(self, *args, **kwargs):
        # print("__doc__")
        return self._overload('__doc__', *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        # print("__eq__")
        return self._overload('__eq__', *args, **kwargs)

    def __finalize__(self, *args, **kwargs):
        # print("__finalize__")
        return self._overload('__finalize__', *args, **kwargs)

    def __float__(self, *args, **kwargs):
        # print("__float__")
        return self._overload('__float__', *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        # print("__floordiv__")
        return self._overload('__floordiv__', *args, **kwargs)

    def __format__(self, *args, **kwargs):
        # print("__format__")
        return self._overload('__format__', *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        # print("__ge__")
        return self._overload('__ge__', *args, **kwargs)

    # def __getattr__(self, *args, **kwargs):
        # # print("__getattr__")
        # return self._overload('__getattr__', *args, **kwargs)

    # def __getattribute__(self, *args, **kwargs):
        # # print("__getattribute__")
        # return self._overload('__getattribute__', *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        # print("__getitem__")
        return self._overload('__getitem__', *args, **kwargs)

    def __getstate__(self, *args, **kwargs):
        # print("__getstate__")
        return self._overload('__getstate__', *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        # print("__gt__")
        return self._overload('__gt__', *args, **kwargs)

    def __hash__(self, *args, **kwargs):
        # print("__hash__")
        return self._overload('__hash__', *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        # print("__iadd__")
        return self._overload('__iadd__', *args, **kwargs)

    def __iand__(self, *args, **kwargs):
        # print("__iand__")
        return self._overload('__iand__', *args, **kwargs)

    def __ifloordiv__(self, *args, **kwargs):
        # print("__ifloordiv__")
        return self._overload('__ifloordiv__', *args, **kwargs)

    def __imod__(self, *args, **kwargs):
        # print("__imod__")
        return self._overload('__imod__', *args, **kwargs)

    def __imul__(self, *args, **kwargs):
        # print("__imul__")
        return self._overload('__imul__', *args, **kwargs)

    # def __init__(self, *args, **kwargs):
        # # print("__init__")
        # return self._overload('__init__', *args, **kwargs)

    def __init_subclass__(self, *args, **kwargs):
        # print("__init_subclass__")
        return self._overload('__init_subclass__', *args, **kwargs)

    def __int__(self, *args, **kwargs):
        # print("__int__")
        return self._overload('__int__', *args, **kwargs)

    def __invert__(self, *args, **kwargs):
        # print("__invert__")
        return self._overload('__invert__', *args, **kwargs)

    def __ior__(self, *args, **kwargs):
        # print("__ior__")
        return self._overload('__ior__', *args, **kwargs)

    def __ipow__(self, *args, **kwargs):
        # print("__ipow__")
        return self._overload('__ipow__', *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        # print("__isub__")
        return self._overload('__isub__', *args, **kwargs)

    def __iter__(self, *args, **kwargs):
        # print("__iter__")
        return self._overload('__iter__', *args, **kwargs)

    def __itruediv__(self, *args, **kwargs):
        # print("__itruediv__")
        return self._overload('__itruediv__', *args, **kwargs)

    def __ixor__(self, *args, **kwargs):
        # print("__ixor__")
        return self._overload('__ixor__', *args, **kwargs)

    def __le__(self, *args, **kwargs):
        # print("__le__")
        return self._overload('__le__', *args, **kwargs)

    def __len__(self, *args, **kwargs):
        # print("__len__")
        return self._overload('__len__', *args, **kwargs)

    def __long__(self, *args, **kwargs):
        # print("__long__")
        return self._overload('__long__', *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        # print("__lt__")
        return self._overload('__lt__', *args, **kwargs)

    def __matmul__(self, *args, **kwargs):
        # print("__matmul__")
        return self._overload('__matmul__', *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        # print("__mod__")
        return self._overload('__mod__', *args, **kwargs)

    def __module__(self, *args, **kwargs):
        # print("__module__")
        return self._overload('__module__', *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        # print("__mul__")
        return self._overload('__mul__', *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        # print("__ne__")
        return self._overload('__ne__', *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        # print("__neg__")
        return self._overload('__neg__', *args, **kwargs)

    # def __new__(self, *args, **kwargs):
        # # print("__new__")
        # return self._overload('__new__', *args, **kwargs)

    def __nonzero__(self, *args, **kwargs):
        # print("__nonzero__")
        return self._overload('__nonzero__', *args, **kwargs)

    def __or__(self, *args, **kwargs):
        # print("__or__")
        return self._overload('__or__', *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        # print("__pos__")
        return self._overload('__pos__', *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        # print("__pow__")
        return self._overload('__pow__', *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        # print("__radd__")
        return self._overload('__radd__', *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        # print("__rand__")
        return self._overload('__rand__', *args, **kwargs)

    def __rdiv__(self, *args, **kwargs):
        # print("__rdiv__")
        return self._overload('__rdiv__', *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        # print("__rdivmod__")
        return self._overload('__rdivmod__', *args, **kwargs)

    def __reduce__(self, *args, **kwargs):
        # print("__reduce__")
        return self._overload('__reduce__', *args, **kwargs)

    def __reduce_ex__(self, *args, **kwargs):
        # print("__reduce_ex__")
        return self._overload('__reduce_ex__', *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        # print("__repr__")
        return self._overload('__repr__', *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        # print("__rfloordiv__")
        return self._overload('__rfloordiv__', *args, **kwargs)

    def __rmatmul__(self, *args, **kwargs):
        # print("__rmatmul__")
        return self._overload('__rmatmul__', *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        # print("__rmod__")
        return self._overload('__rmod__', *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        # print("__rmul__")
        return self._overload('__rmul__', *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        # print("__ror__")
        return self._overload('__ror__', *args, **kwargs)

    def __round__(self, *args, **kwargs):
        # print("__round__")
        return self._overload('__round__', *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        # print("__rpow__")
        return self._overload('__rpow__', *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        # print("__rsub__")
        return self._overload('__rsub__', *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        # print("__rtruediv__")
        return self._overload('__rtruediv__', *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        # print("__rxor__")
        return self._overload('__rxor__', *args, **kwargs)

    # def __setattr__(self, *args, **kwargs):
        # # print("__setattr__")
        # return self._overload('__setattr__', *args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        # print("__setitem__")
        return self._overload('__setitem__', *args, **kwargs)

    def __setstate__(self, *args, **kwargs):
        # print("__setstate__")
        return self._overload('__setstate__', *args, **kwargs)

    def __sizeof__(self, *args, **kwargs):
        # print("__sizeof__")
        return self._overload('__sizeof__', *args, **kwargs)

    def __str__(self, *args, **kwargs):
        # print("__str__")
        return self._overload('__str__', *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        # print("__sub__")
        return self._overload('__sub__', *args, **kwargs)

    def __subclasshook__(self, *args, **kwargs):
        # print("__subclasshook__")
        return self._overload('__subclasshook__', *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        # print("__truediv__")
        return self._overload('__truediv__', *args, **kwargs)

    def __unicode__(self, *args, **kwargs):
        # print("__unicode__")
        return self._overload('__unicode__', *args, **kwargs)

    def __weakref__(self, *args, **kwargs):
        # print("__weakref__")
        return self._overload('__weakref__', *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        # print("__xor__")
        return self._overload('__xor__', *args, **kwargs)

    def _accessors(self, *args, **kwargs):
        # print("_accessors")
        return self._overload('_accessors', *args, **kwargs)

    def _add_numeric_operations(self, *args, **kwargs):
        # print("_add_numeric_operations")
        return self._overload('_add_numeric_operations', *args, **kwargs)

    def _add_series_only_operations(self, *args, **kwargs):
        # print("_add_series_only_operations")
        return self._overload('_add_series_only_operations', *args, **kwargs)

    def _add_series_or_dataframe_operations(self, *args, **kwargs):
        # print("_add_series_or_dataframe_operations")
        return self._overload('_add_series_or_dataframe_operations', *args, **kwargs)

    def _agg_by_level(self, *args, **kwargs):
        # print("_agg_by_level")
        return self._overload('_agg_by_level', *args, **kwargs)

    def _agg_examples_doc(self, *args, **kwargs):
        # print("_agg_examples_doc")
        return self._overload('_agg_examples_doc', *args, **kwargs)

    def _agg_see_also_doc(self, *args, **kwargs):
        # print("_agg_see_also_doc")
        return self._overload('_agg_see_also_doc', *args, **kwargs)

    def _aggregate(self, *args, **kwargs):
        # print("_aggregate")
        return self._overload('_aggregate', *args, **kwargs)

    def _aggregate_multiple_funcs(self, *args, **kwargs):
        # print("_aggregate_multiple_funcs")
        return self._overload('_aggregate_multiple_funcs', *args, **kwargs)

    def _align_frame(self, *args, **kwargs):
        # print("_align_frame")
        return self._overload('_align_frame', *args, **kwargs)

    def _align_series(self, *args, **kwargs):
        # print("_align_series")
        return self._overload('_align_series', *args, **kwargs)

    def _binop(self, *args, **kwargs):
        # print("_binop")
        return self._overload('_binop', *args, **kwargs)

    def _box_item_values(self, *args, **kwargs):
        # print("_box_item_values")
        return self._overload('_box_item_values', *args, **kwargs)

    def _builtin_table(self, *args, **kwargs):
        # print("_builtin_table")
        return self._overload('_builtin_table', *args, **kwargs)

    def _can_hold_na(self, *args, **kwargs):
        # print("_can_hold_na")
        return self._overload('_can_hold_na', *args, **kwargs)

    def _check_inplace_setting(self, *args, **kwargs):
        # print("_check_inplace_setting")
        return self._overload('_check_inplace_setting', *args, **kwargs)

    def _check_is_chained_assignment_possible(self, *args, **kwargs):
        # print("_check_is_chained_assignment_possible")
        return self._overload('_check_is_chained_assignment_possible', *args, **kwargs)

    def _check_label_or_level_ambiguity(self, *args, **kwargs):
        # print("_check_label_or_level_ambiguity")
        return self._overload('_check_label_or_level_ambiguity', *args, **kwargs)

    def _check_percentile(self, *args, **kwargs):
        # print("_check_percentile")
        return self._overload('_check_percentile', *args, **kwargs)

    def _check_setitem_copy(self, *args, **kwargs):
        # print("_check_setitem_copy")
        return self._overload('_check_setitem_copy', *args, **kwargs)

    def _clear_item_cache(self, *args, **kwargs):
        # print("_clear_item_cache")
        return self._overload('_clear_item_cache', *args, **kwargs)

    def _clip_with_one_bound(self, *args, **kwargs):
        # print("_clip_with_one_bound")
        return self._overload('_clip_with_one_bound', *args, **kwargs)

    def _clip_with_scalar(self, *args, **kwargs):
        # print("_clip_with_scalar")
        return self._overload('_clip_with_scalar', *args, **kwargs)

    def _consolidate(self, *args, **kwargs):
        # print("_consolidate")
        return self._overload('_consolidate', *args, **kwargs)

    def _consolidate_inplace(self, *args, **kwargs):
        # print("_consolidate_inplace")
        return self._overload('_consolidate_inplace', *args, **kwargs)

    def _construct_axes_dict(self, *args, **kwargs):
        # print("_construct_axes_dict")
        return self._overload('_construct_axes_dict', *args, **kwargs)

    def _construct_axes_dict_for_slice(self, *args, **kwargs):
        # print("_construct_axes_dict_for_slice")
        return self._overload('_construct_axes_dict_for_slice', *args, **kwargs)

    def _construct_axes_dict_from(self, *args, **kwargs):
        # print("_construct_axes_dict_from")
        return self._overload('_construct_axes_dict_from', *args, **kwargs)

    def _construct_axes_from_arguments(self, *args, **kwargs):
        # print("_construct_axes_from_arguments")
        return self._overload('_construct_axes_from_arguments', *args, **kwargs)

    def _constructor(self, *args, **kwargs):
        # print("_constructor")
        return self._overload('_constructor', *args, **kwargs)

    def _constructor_expanddim(self, *args, **kwargs):
        # print("_constructor_expanddim")
        return self._overload('_constructor_expanddim', *args, **kwargs)

    def _constructor_sliced(self, *args, **kwargs):
        # print("_constructor_sliced")
        return self._overload('_constructor_sliced', *args, **kwargs)

    def _convert(self, *args, **kwargs):
        # print("_convert")
        return self._overload('_convert', *args, **kwargs)

    def _create_indexer(self, *args, **kwargs):
        # print("_create_indexer")
        return self._overload('_create_indexer', *args, **kwargs)

    def _cython_table(self, *args, **kwargs):
        # print("_cython_table")
        return self._overload('_cython_table', *args, **kwargs)

    def _deprecations(self, *args, **kwargs):
        # print("_deprecations")
        return self._overload('_deprecations', *args, **kwargs)

    def _dir_additions(self, *args, **kwargs):
        # print("_dir_additions")
        return self._overload('_dir_additions', *args, **kwargs)

    def _dir_deletions(self, *args, **kwargs):
        # print("_dir_deletions")
        return self._overload('_dir_deletions', *args, **kwargs)

    def _drop_axis(self, *args, **kwargs):
        # print("_drop_axis")
        return self._overload('_drop_axis', *args, **kwargs)

    def _drop_labels_or_levels(self, *args, **kwargs):
        # print("_drop_labels_or_levels")
        return self._overload('_drop_labels_or_levels', *args, **kwargs)

    def _expand_axes(self, *args, **kwargs):
        # print("_expand_axes")
        return self._overload('_expand_axes', *args, **kwargs)

    def _find_valid_index(self, *args, **kwargs):
        # print("_find_valid_index")
        return self._overload('_find_valid_index', *args, **kwargs)

    def _formatting_values(self, *args, **kwargs):
        # print("_formatting_values")
        return self._overload('_formatting_values', *args, **kwargs)

    def _from_axes(self, *args, **kwargs):
        # print("_from_axes")
        return self._overload('_from_axes', *args, **kwargs)

    def _get_axis(self, *args, **kwargs):
        # print("_get_axis")
        return self._overload('_get_axis', *args, **kwargs)

    def _get_axis_name(self, *args, **kwargs):
        # print("_get_axis_name")
        return self._overload('_get_axis_name', *args, **kwargs)

    def _get_axis_number(self, *args, **kwargs):
        # print("_get_axis_number")
        return self._overload('_get_axis_number', *args, **kwargs)

    def _get_axis_resolvers(self, *args, **kwargs):
        # print("_get_axis_resolvers")
        return self._overload('_get_axis_resolvers', *args, **kwargs)

    def _get_block_manager_axis(self, *args, **kwargs):
        # print("_get_block_manager_axis")
        return self._overload('_get_block_manager_axis', *args, **kwargs)

    def _get_bool_data(self, *args, **kwargs):
        # print("_get_bool_data")
        return self._overload('_get_bool_data', *args, **kwargs)

    def _get_cacher(self, *args, **kwargs):
        # print("_get_cacher")
        return self._overload('_get_cacher', *args, **kwargs)

    def _get_index_resolvers(self, *args, **kwargs):
        # print("_get_index_resolvers")
        return self._overload('_get_index_resolvers', *args, **kwargs)

    def _get_item_cache(self, *args, **kwargs):
        # print("_get_item_cache")
        return self._overload('_get_item_cache', *args, **kwargs)

    def _get_label_or_level_values(self, *args, **kwargs):
        # print("_get_label_or_level_values")
        return self._overload('_get_label_or_level_values', *args, **kwargs)

    def _get_numeric_data(self, *args, **kwargs):
        # print("_get_numeric_data")
        return self._overload('_get_numeric_data', *args, **kwargs)

    def _get_value(self, *args, **kwargs):
        # print("_get_value")
        return self._overload('_get_value', *args, **kwargs)

    def _get_values(self, *args, **kwargs):
        # print("_get_values")
        return self._overload('_get_values', *args, **kwargs)

    def _get_values_tuple(self, *args, **kwargs):
        # print("_get_values_tuple")
        return self._overload('_get_values_tuple', *args, **kwargs)

    def _get_with(self, *args, **kwargs):
        # print("_get_with")
        return self._overload('_get_with', *args, **kwargs)

    def _gotitem(self, *args, **kwargs):
        # print("_gotitem")
        return self._overload('_gotitem', *args, **kwargs)

    def _iget_item_cache(self, *args, **kwargs):
        # print("_iget_item_cache")
        return self._overload('_iget_item_cache', *args, **kwargs)

    def _index(self, *args, **kwargs):
        # print("_index")
        return self._overload('_index', *args, **kwargs)

    def _indexed_same(self, *args, **kwargs):
        # print("_indexed_same")
        return self._overload('_indexed_same', *args, **kwargs)

    def _info_axis(self, *args, **kwargs):
        # print("_info_axis")
        return self._overload('_info_axis', *args, **kwargs)

    def _info_axis_name(self, *args, **kwargs):
        # print("_info_axis_name")
        return self._overload('_info_axis_name', *args, **kwargs)

    def _info_axis_number(self, *args, **kwargs):
        # print("_info_axis_number")
        return self._overload('_info_axis_number', *args, **kwargs)

    def _init_dict(self, *args, **kwargs):
        # print("_init_dict")
        return self._overload('_init_dict', *args, **kwargs)

    def _init_mgr(self, *args, **kwargs):
        # print("_init_mgr")
        return self._overload('_init_mgr', *args, **kwargs)

    def _internal_names(self, *args, **kwargs):
        # print("_internal_names")
        return self._overload('_internal_names', *args, **kwargs)

    def _internal_names_set(self, *args, **kwargs):
        # print("_internal_names_set")
        return self._overload('_internal_names_set', *args, **kwargs)

    def _is_builtin_func(self, *args, **kwargs):
        # print("_is_builtin_func")
        return self._overload('_is_builtin_func', *args, **kwargs)

    def _is_cached(self, *args, **kwargs):
        # print("_is_cached")
        return self._overload('_is_cached', *args, **kwargs)

    def _is_copy(self, *args, **kwargs):
        # print("_is_copy")
        return self._overload('_is_copy', *args, **kwargs)

    def _is_cython_func(self, *args, **kwargs):
        # print("_is_cython_func")
        return self._overload('_is_cython_func', *args, **kwargs)

    def _is_datelike_mixed_type(self, *args, **kwargs):
        # print("_is_datelike_mixed_type")
        return self._overload('_is_datelike_mixed_type', *args, **kwargs)

    def _is_homogeneous_type(self, *args, **kwargs):
        # print("_is_homogeneous_type")
        return self._overload('_is_homogeneous_type', *args, **kwargs)

    def _is_label_or_level_reference(self, *args, **kwargs):
        # print("_is_label_or_level_reference")
        return self._overload('_is_label_or_level_reference', *args, **kwargs)

    def _is_label_reference(self, *args, **kwargs):
        # print("_is_label_reference")
        return self._overload('_is_label_reference', *args, **kwargs)

    def _is_level_reference(self, *args, **kwargs):
        # print("_is_level_reference")
        return self._overload('_is_level_reference', *args, **kwargs)

    def _is_mixed_type(self, *args, **kwargs):
        # print("_is_mixed_type")
        return self._overload('_is_mixed_type', *args, **kwargs)

    def _is_numeric_mixed_type(self, *args, **kwargs):
        # print("_is_numeric_mixed_type")
        return self._overload('_is_numeric_mixed_type', *args, **kwargs)

    def _is_view(self, *args, **kwargs):
        # print("_is_view")
        return self._overload('_is_view', *args, **kwargs)

    def _ix(self, *args, **kwargs):
        # print("_ix")
        return self._overload('_ix', *args, **kwargs)

    def _ixs(self, *args, **kwargs):
        # print("_ixs")
        return self._overload('_ixs', *args, **kwargs)

    def _map_values(self, *args, **kwargs):
        # print("_map_values")
        return self._overload('_map_values', *args, **kwargs)

    def _maybe_cache_changed(self, *args, **kwargs):
        # print("_maybe_cache_changed")
        return self._overload('_maybe_cache_changed', *args, **kwargs)

    def _maybe_update_cacher(self, *args, **kwargs):
        # print("_maybe_update_cacher")
        return self._overload('_maybe_update_cacher', *args, **kwargs)

    def _metadata(self, *args, **kwargs):
        # print("_metadata")
        return self._overload('_metadata', *args, **kwargs)

    def _ndarray_values(self, *args, **kwargs):
        # print("_ndarray_values")
        return self._overload('_ndarray_values', *args, **kwargs)

    def _needs_reindex_multi(self, *args, **kwargs):
        # print("_needs_reindex_multi")
        return self._overload('_needs_reindex_multi', *args, **kwargs)

    def _obj_with_exclusions(self, *args, **kwargs):
        # print("_obj_with_exclusions")
        return self._overload('_obj_with_exclusions', *args, **kwargs)

    def _protect_consolidate(self, *args, **kwargs):
        # print("_protect_consolidate")
        return self._overload('_protect_consolidate', *args, **kwargs)

    def _reduce(self, *args, **kwargs):
        # print("_reduce")
        return self._overload('_reduce', *args, **kwargs)

    def _reindex_axes(self, *args, **kwargs):
        # print("_reindex_axes")
        return self._overload('_reindex_axes', *args, **kwargs)

    def _reindex_indexer(self, *args, **kwargs):
        # print("_reindex_indexer")
        return self._overload('_reindex_indexer', *args, **kwargs)

    def _reindex_multi(self, *args, **kwargs):
        # print("_reindex_multi")
        return self._overload('_reindex_multi', *args, **kwargs)

    def _reindex_with_indexers(self, *args, **kwargs):
        # print("_reindex_with_indexers")
        return self._overload('_reindex_with_indexers', *args, **kwargs)

    def _repr_data_resource_(self, *args, **kwargs):
        # print("_repr_data_resource_")
        return self._overload('_repr_data_resource_', *args, **kwargs)

    def _repr_latex_(self, *args, **kwargs):
        # print("_repr_latex_")
        return self._overload('_repr_latex_', *args, **kwargs)

    def _reset_cache(self, *args, **kwargs):
        # print("_reset_cache")
        return self._overload('_reset_cache', *args, **kwargs)

    def _reset_cacher(self, *args, **kwargs):
        # print("_reset_cacher")
        return self._overload('_reset_cacher', *args, **kwargs)

    def _selected_obj(self, *args, **kwargs):
        # print("_selected_obj")
        return self._overload('_selected_obj', *args, **kwargs)

    def _selection(self, *args, **kwargs):
        # print("_selection")
        return self._overload('_selection', *args, **kwargs)

    def _selection_list(self, *args, **kwargs):
        # print("_selection_list")
        return self._overload('_selection_list', *args, **kwargs)

    def _selection_name(self, *args, **kwargs):
        # print("_selection_name")
        return self._overload('_selection_name', *args, **kwargs)

    def _set_as_cached(self, *args, **kwargs):
        # print("_set_as_cached")
        return self._overload('_set_as_cached', *args, **kwargs)

    def _set_axis(self, *args, **kwargs):
        # print("_set_axis")
        return self._overload('_set_axis', *args, **kwargs)

    def _set_axis_name(self, *args, **kwargs):
        # print("_set_axis_name")
        return self._overload('_set_axis_name', *args, **kwargs)

    def _set_is_copy(self, *args, **kwargs):
        # print("_set_is_copy")
        return self._overload('_set_is_copy', *args, **kwargs)

    def _set_item(self, *args, **kwargs):
        # print("_set_item")
        return self._overload('_set_item', *args, **kwargs)

    def _set_labels(self, *args, **kwargs):
        # print("_set_labels")
        return self._overload('_set_labels', *args, **kwargs)

    def _set_name(self, *args, **kwargs):
        # print("_set_name")
        return self._overload('_set_name', *args, **kwargs)

    def _set_subtyp(self, *args, **kwargs):
        # print("_set_subtyp")
        return self._overload('_set_subtyp', *args, **kwargs)

    def _set_value(self, *args, **kwargs):
        # print("_set_value")
        return self._overload('_set_value', *args, **kwargs)

    def _set_values(self, *args, **kwargs):
        # print("_set_values")
        return self._overload('_set_values', *args, **kwargs)

    def _set_with(self, *args, **kwargs):
        # print("_set_with")
        return self._overload('_set_with', *args, **kwargs)

    def _set_with_engine(self, *args, **kwargs):
        # print("_set_with_engine")
        return self._overload('_set_with_engine', *args, **kwargs)

    def _setup_axes(self, *args, **kwargs):
        # print("_setup_axes")
        return self._overload('_setup_axes', *args, **kwargs)

    def _shallow_copy(self, *args, **kwargs):
        # print("_shallow_copy")
        return self._overload('_shallow_copy', *args, **kwargs)

    def _slice(self, *args, **kwargs):
        # print("_slice")
        return self._overload('_slice', *args, **kwargs)

    def _stat_axis(self, *args, **kwargs):
        # print("_stat_axis")
        return self._overload('_stat_axis', *args, **kwargs)

    def _stat_axis_name(self, *args, **kwargs):
        # print("_stat_axis_name")
        return self._overload('_stat_axis_name', *args, **kwargs)

    def _stat_axis_number(self, *args, **kwargs):
        # print("_stat_axis_number")
        return self._overload('_stat_axis_number', *args, **kwargs)

    def _take(self, *args, **kwargs):
        # print("_take")
        return self._overload('_take', *args, **kwargs)

    def _to_dict_of_blocks(self, *args, **kwargs):
        # print("_to_dict_of_blocks")
        return self._overload('_to_dict_of_blocks', *args, **kwargs)

    def _try_aggregate_string_function(self, *args, **kwargs):
        # print("_try_aggregate_string_function")
        return self._overload('_try_aggregate_string_function', *args, **kwargs)

    def _typ(self, *args, **kwargs):
        # print("_typ")
        return self._overload('_typ', *args, **kwargs)

    def _unpickle_series_compat(self, *args, **kwargs):
        # print("_unpickle_series_compat")
        return self._overload('_unpickle_series_compat', *args, **kwargs)

    def _update_inplace(self, *args, **kwargs):
        # print("_update_inplace")
        return self._overload('_update_inplace', *args, **kwargs)

    def _validate_dtype(self, *args, **kwargs):
        # print("_validate_dtype")
        return self._overload('_validate_dtype', *args, **kwargs)

    def _values(self, *args, **kwargs):
        # print("_values")
        return self._overload('_values', *args, **kwargs)

    def _where(self, *args, **kwargs):
        # print("_where")
        return self._overload('_where', *args, **kwargs)

    def _xs(self, *args, **kwargs):
        # print("_xs")
        return self._overload('_xs', *args, **kwargs)

    def abs(self, *args, **kwargs):
        # print("abs")
        return self._overload('abs', *args, **kwargs)

    def add(self, *args, **kwargs):
        # print("add")
        return self._overload('add', *args, **kwargs)

    def add_prefix(self, *args, **kwargs):
        # print("add_prefix")
        return self._overload('add_prefix', *args, **kwargs)

    def add_suffix(self, *args, **kwargs):
        # print("add_suffix")
        return self._overload('add_suffix', *args, **kwargs)

    def agg(self, *args, **kwargs):
        # print("agg")
        return self._overload('agg', *args, **kwargs)

    def aggregate(self, *args, **kwargs):
        # print("aggregate")
        return self._overload('aggregate', *args, **kwargs)

    def align(self, *args, **kwargs):
        # print("align")
        return self._overload('align', *args, **kwargs)

    def all(self, *args, **kwargs):
        # print("all")
        return self._overload('all', *args, **kwargs)

    def any(self, *args, **kwargs):
        # print("any")
        return self._overload('any', *args, **kwargs)

    def append(self, *args, **kwargs):
        # print("append")
        return self._overload('append', *args, **kwargs)

    def apply(self, *args, **kwargs):
        # print("apply")
        return self._overload('apply', *args, **kwargs)

    def argmax(self, *args, **kwargs):
        # print("argmax")
        return self._overload('argmax', *args, **kwargs)

    def argmin(self, *args, **kwargs):
        # print("argmin")
        return self._overload('argmin', *args, **kwargs)

    def argsort(self, *args, **kwargs):
        # print("argsort")
        return self._overload('argsort', *args, **kwargs)

    def array(self, *args, **kwargs):
        # print("array")
        return self._overload('array', *args, **kwargs)

    def as_matrix(self, *args, **kwargs):
        # print("as_matrix")
        return self._overload('as_matrix', *args, **kwargs)

    def asfreq(self, *args, **kwargs):
        # print("asfreq")
        return self._overload('asfreq', *args, **kwargs)

    def asof(self, *args, **kwargs):
        # print("asof")
        return self._overload('asof', *args, **kwargs)

    def astype(self, *args, **kwargs):
        # print("astype")
        return self._overload('astype', *args, **kwargs)

    def at(self, *args, **kwargs):
        # print("at")
        return self._overload('at', *args, **kwargs)

    def at_time(self, *args, **kwargs):
        # print("at_time")
        return self._overload('at_time', *args, **kwargs)

    def autocorr(self, *args, **kwargs):
        # print("autocorr")
        return self._overload('autocorr', *args, **kwargs)

    def axes(self, *args, **kwargs):
        # print("axes")
        return self._overload('axes', *args, **kwargs)

    def base(self, *args, **kwargs):
        # print("base")
        return self._overload('base', *args, **kwargs)

    def between(self, *args, **kwargs):
        # print("between")
        return self._overload('between', *args, **kwargs)

    def between_time(self, *args, **kwargs):
        # print("between_time")
        return self._overload('between_time', *args, **kwargs)

    def bfill(self, *args, **kwargs):
        # print("bfill")
        return self._overload('bfill', *args, **kwargs)

    def bool(self, *args, **kwargs):
        # print("bool")
        return self._overload('bool', *args, **kwargs)

    def clip(self, *args, **kwargs):
        # print("clip")
        return self._overload('clip', *args, **kwargs)

    def clip_lower(self, *args, **kwargs):
        # print("clip_lower")
        return self._overload('clip_lower', *args, **kwargs)

    def clip_upper(self, *args, **kwargs):
        # print("clip_upper")
        return self._overload('clip_upper', *args, **kwargs)

    def combine(self, *args, **kwargs):
        # print("combine")
        return self._overload('combine', *args, **kwargs)

    def combine_first(self, *args, **kwargs):
        # print("combine_first")
        return self._overload('combine_first', *args, **kwargs)

    def compound(self, *args, **kwargs):
        # print("compound")
        return self._overload('compound', *args, **kwargs)

    def compress(self, *args, **kwargs):
        # print("compress")
        return self._overload('compress', *args, **kwargs)

    def copy(self, *args, **kwargs):
        # print("copy")
        return self._overload('copy', *args, **kwargs)

    def corr(self, *args, **kwargs):
        # print("corr")
        return self._overload('corr', *args, **kwargs)

    def count(self, *args, **kwargs):
        # print("count")
        return self._overload('count', *args, **kwargs)

    def cov(self, *args, **kwargs):
        # print("cov")
        return self._overload('cov', *args, **kwargs)

    def cummax(self, *args, **kwargs):
        # print("cummax")
        return self._overload('cummax', *args, **kwargs)

    def cummin(self, *args, **kwargs):
        # print("cummin")
        return self._overload('cummin', *args, **kwargs)

    def cumprod(self, *args, **kwargs):
        # print("cumprod")
        return self._overload('cumprod', *args, **kwargs)

    def cumsum(self, *args, **kwargs):
        # print("cumsum")
        return self._overload('cumsum', *args, **kwargs)

    def data(self, *args, **kwargs):
        # print("data")
        return self._overload('data', *args, **kwargs)

    def describe(self, *args, **kwargs):
        # print("describe")
        return self._overload('describe', *args, **kwargs)

    def diff(self, *args, **kwargs):
        # print("diff")
        return self._overload('diff', *args, **kwargs)

    def div(self, *args, **kwargs):
        # print("div")
        return self._overload('div', *args, **kwargs)

    def divide(self, *args, **kwargs):
        # print("divide")
        return self._overload('divide', *args, **kwargs)

    def divmod(self, *args, **kwargs):
        # print("divmod")
        return self._overload('divmod', *args, **kwargs)

    def dot(self, *args, **kwargs):
        # print("dot")
        return self._overload('dot', *args, **kwargs)

    def drop(self, *args, **kwargs):
        # print("drop")
        return self._overload('drop', *args, **kwargs)

    def drop_duplicates(self, *args, **kwargs):
        # print("drop_duplicates")
        return self._overload('drop_duplicates', *args, **kwargs)

    def droplevel(self, *args, **kwargs):
        # print("droplevel")
        return self._overload('droplevel', *args, **kwargs)

    def dropna(self, *args, **kwargs):
        # print("dropna")
        return self._overload('dropna', *args, **kwargs)

    def dtype(self, *args, **kwargs):
        # print("dtype")
        return self._overload('dtype', *args, **kwargs)

    def dtypes(self, *args, **kwargs):
        # print("dtypes")
        return self._overload('dtypes', *args, **kwargs)

    def duplicated(self, *args, **kwargs):
        # print("duplicated")
        return self._overload('duplicated', *args, **kwargs)

    def empty(self, *args, **kwargs):
        # print("empty")
        return self._overload('empty', *args, **kwargs)

    def eq(self, *args, **kwargs):
        # print("eq")
        return self._overload('eq', *args, **kwargs)

    def equals(self, *args, **kwargs):
        # print("equals")
        return self._overload('equals', *args, **kwargs)

    def ewm(self, *args, **kwargs):
        # print("ewm")
        return self._overload('ewm', *args, **kwargs)

    def expanding(self, *args, **kwargs):
        # print("expanding")
        return self._overload('expanding', *args, **kwargs)

    def factorize(self, *args, **kwargs):
        # print("factorize")
        return self._overload('factorize', *args, **kwargs)

    def ffill(self, *args, **kwargs):
        # print("ffill")
        return self._overload('ffill', *args, **kwargs)

    def fillna(self, *args, **kwargs):
        # print("fillna")
        return self._overload('fillna', *args, **kwargs)

    def filter(self, *args, **kwargs):
        # print("filter")
        return self._overload('filter', *args, **kwargs)

    def first(self, *args, **kwargs):
        # print("first")
        return self._overload('first', *args, **kwargs)

    def first_valid_index(self, *args, **kwargs):
        # print("first_valid_index")
        return self._overload('first_valid_index', *args, **kwargs)

    def flags(self, *args, **kwargs):
        # print("flags")
        return self._overload('flags', *args, **kwargs)

    def floordiv(self, *args, **kwargs):
        # print("floordiv")
        return self._overload('floordiv', *args, **kwargs)

    def from_array(self, *args, **kwargs):
        # print("from_array")
        return self._overload('from_array', *args, **kwargs)

    def ftype(self, *args, **kwargs):
        # print("ftype")
        return self._overload('ftype', *args, **kwargs)

    def ftypes(self, *args, **kwargs):
        # print("ftypes")
        return self._overload('ftypes', *args, **kwargs)

    def ge(self, *args, **kwargs):
        # print("ge")
        return self._overload('ge', *args, **kwargs)

    def get(self, *args, **kwargs):
        # print("get")
        return self._overload('get', *args, **kwargs)

    def get_dtype_counts(self, *args, **kwargs):
        # print("get_dtype_counts")
        return self._overload('get_dtype_counts', *args, **kwargs)

    def get_ftype_counts(self, *args, **kwargs):
        # print("get_ftype_counts")
        return self._overload('get_ftype_counts', *args, **kwargs)

    def get_values(self, *args, **kwargs):
        # print("get_values")
        return self._overload('get_values', *args, **kwargs)

    def groupby(self, *args, **kwargs):
        # print("groupby")
        return self._overload('groupby', *args, **kwargs)

    def gt(self, *args, **kwargs):
        # print("gt")
        return self._overload('gt', *args, **kwargs)

    def hasnans(self, *args, **kwargs):
        # print("hasnans")
        return self._overload('hasnans', *args, **kwargs)

    def head(self, *args, **kwargs):
        # print("head")
        return self._overload('head', *args, **kwargs)

    def hist(self, *args, **kwargs):
        # print("hist")
        return self._overload('hist', *args, **kwargs)

    def iat(self, *args, **kwargs):
        # print("iat")
        return self._overload('iat', *args, **kwargs)

    def idxmax(self, *args, **kwargs):
        # print("idxmax")
        return self._overload('idxmax', *args, **kwargs)

    def idxmin(self, *args, **kwargs):
        # print("idxmin")
        return self._overload('idxmin', *args, **kwargs)

    def iloc(self, *args, **kwargs):
        # print("iloc")
        return self._overload('iloc', *args, **kwargs)

    def imag(self, *args, **kwargs):
        # print("imag")
        return self._overload('imag', *args, **kwargs)

    def index(self, *args, **kwargs):
        # print("index")
        return self._overload('index', *args, **kwargs)

    def infer_objects(self, *args, **kwargs):
        # print("infer_objects")
        return self._overload('infer_objects', *args, **kwargs)

    def interpolate(self, *args, **kwargs):
        # print("interpolate")
        return self._overload('interpolate', *args, **kwargs)

    def is_monotonic(self, *args, **kwargs):
        # print("is_monotonic")
        return self._overload('is_monotonic', *args, **kwargs)

    def is_monotonic_decreasing(self, *args, **kwargs):
        # print("is_monotonic_decreasing")
        return self._overload('is_monotonic_decreasing', *args, **kwargs)

    def is_monotonic_increasing(self, *args, **kwargs):
        # print("is_monotonic_increasing")
        return self._overload('is_monotonic_increasing', *args, **kwargs)

    def is_unique(self, *args, **kwargs):
        # print("is_unique")
        return self._overload('is_unique', *args, **kwargs)

    def isin(self, *args, **kwargs):
        # print("isin")
        return self._overload('isin', *args, **kwargs)

    def isna(self, *args, **kwargs):
        # print("isna")
        return self._overload('isna', *args, **kwargs)

    def isnull(self, *args, **kwargs):
        # print("isnull")
        return self._overload('isnull', *args, **kwargs)

    def item(self, *args, **kwargs):
        # print("item")
        return self._overload('item', *args, **kwargs)

    def items(self, *args, **kwargs):
        # print("items")
        return self._overload('items', *args, **kwargs)

    def itemsize(self, *args, **kwargs):
        # print("itemsize")
        return self._overload('itemsize', *args, **kwargs)

    def iteritems(self, *args, **kwargs):
        # print("iteritems")
        return self._overload('iteritems', *args, **kwargs)

    def ix(self, *args, **kwargs):
        # print("ix")
        return self._overload('ix', *args, **kwargs)

    def keys(self, *args, **kwargs):
        # print("keys")
        return self._overload('keys', *args, **kwargs)

    def kurt(self, *args, **kwargs):
        # print("kurt")
        return self._overload('kurt', *args, **kwargs)

    def kurtosis(self, *args, **kwargs):
        # print("kurtosis")
        return self._overload('kurtosis', *args, **kwargs)

    def last(self, *args, **kwargs):
        # print("last")
        return self._overload('last', *args, **kwargs)

    def last_valid_index(self, *args, **kwargs):
        # print("last_valid_index")
        return self._overload('last_valid_index', *args, **kwargs)

    def le(self, *args, **kwargs):
        # print("le")
        return self._overload('le', *args, **kwargs)

    def loc(self, *args, **kwargs):
        # print("loc")
        return self._overload('loc', *args, **kwargs)

    def lt(self, *args, **kwargs):
        # print("lt")
        return self._overload('lt', *args, **kwargs)

    def mad(self, *args, **kwargs):
        # print("mad")
        return self._overload('mad', *args, **kwargs)

    def map(self, *args, **kwargs):
        # print("map")
        return self._overload('map', *args, **kwargs)

    def mask(self, *args, **kwargs):
        # print("mask")
        return self._overload('mask', *args, **kwargs)

    def max(self, *args, **kwargs):
        # print("max")
        return self._overload('max', *args, **kwargs)

    def mean(self, *args, **kwargs):
        # print("mean")
        return self._overload('mean', *args, **kwargs)

    def median(self, *args, **kwargs):
        # print("median")
        return self._overload('median', *args, **kwargs)

    def memory_usage(self, *args, **kwargs):
        # print("memory_usage")
        return self._overload('memory_usage', *args, **kwargs)

    def min(self, *args, **kwargs):
        # print("min")
        return self._overload('min', *args, **kwargs)

    def mod(self, *args, **kwargs):
        # print("mod")
        return self._overload('mod', *args, **kwargs)

    def mode(self, *args, **kwargs):
        # print("mode")
        return self._overload('mode', *args, **kwargs)

    def mul(self, *args, **kwargs):
        # print("mul")
        return self._overload('mul', *args, **kwargs)

    def multiply(self, *args, **kwargs):
        # print("multiply")
        return self._overload('multiply', *args, **kwargs)

    def name(self, *args, **kwargs):
        # print("name")
        return self._overload('name', *args, **kwargs)

    def nbytes(self, *args, **kwargs):
        # print("nbytes")
        return self._overload('nbytes', *args, **kwargs)

    def ndim(self, *args, **kwargs):
        # print("ndim")
        return self._overload('ndim', *args, **kwargs)

    def ne(self, *args, **kwargs):
        # print("ne")
        return self._overload('ne', *args, **kwargs)

    def nlargest(self, *args, **kwargs):
        # print("nlargest")
        return self._overload('nlargest', *args, **kwargs)

    def nonzero(self, *args, **kwargs):
        # print("nonzero")
        return self._overload('nonzero', *args, **kwargs)

    def notna(self, *args, **kwargs):
        # print("notna")
        return self._overload('notna', *args, **kwargs)

    def notnull(self, *args, **kwargs):
        # print("notnull")
        return self._overload('notnull', *args, **kwargs)

    def nsmallest(self, *args, **kwargs):
        # print("nsmallest")
        return self._overload('nsmallest', *args, **kwargs)

    def nunique(self, *args, **kwargs):
        # print("nunique")
        return self._overload('nunique', *args, **kwargs)

    def pct_change(self, *args, **kwargs):
        # print("pct_change")
        return self._overload('pct_change', *args, **kwargs)

    def pipe(self, *args, **kwargs):
        # print("pipe")
        return self._overload('pipe', *args, **kwargs)

    def plot(self, *args, **kwargs):
        # print("plot")
        return self._overload('plot', *args, **kwargs)

    def pop(self, *args, **kwargs):
        # print("pop")
        return self._overload('pop', *args, **kwargs)

    def pow(self, *args, **kwargs):
        # print("pow")
        return self._overload('pow', *args, **kwargs)

    def prod(self, *args, **kwargs):
        # print("prod")
        return self._overload('prod', *args, **kwargs)

    def product(self, *args, **kwargs):
        # print("product")
        return self._overload('product', *args, **kwargs)

    def ptp(self, *args, **kwargs):
        # print("ptp")
        return self._overload('ptp', *args, **kwargs)

    def put(self, *args, **kwargs):
        # print("put")
        return self._overload('put', *args, **kwargs)

    def quantile(self, *args, **kwargs):
        # print("quantile")
        return self._overload('quantile', *args, **kwargs)

    def radd(self, *args, **kwargs):
        # print("radd")
        return self._overload('radd', *args, **kwargs)

    def rank(self, *args, **kwargs):
        # print("rank")
        return self._overload('rank', *args, **kwargs)

    def ravel(self, *args, **kwargs):
        # print("ravel")
        return self._overload('ravel', *args, **kwargs)

    def rdiv(self, *args, **kwargs):
        # print("rdiv")
        return self._overload('rdiv', *args, **kwargs)

    def rdivmod(self, *args, **kwargs):
        # print("rdivmod")
        return self._overload('rdivmod', *args, **kwargs)

    def real(self, *args, **kwargs):
        # print("real")
        return self._overload('real', *args, **kwargs)

    def reindex(self, *args, **kwargs):
        # print("reindex")
        return self._overload('reindex', *args, **kwargs)

    def reindex_axis(self, *args, **kwargs):
        # print("reindex_axis")
        return self._overload('reindex_axis', *args, **kwargs)

    def reindex_like(self, *args, **kwargs):
        # print("reindex_like")
        return self._overload('reindex_like', *args, **kwargs)

    def rename(self, *args, **kwargs):
        # print("rename")
        return self._overload('rename', *args, **kwargs)

    def rename_axis(self, *args, **kwargs):
        # print("rename_axis")
        return self._overload('rename_axis', *args, **kwargs)

    def reorder_levels(self, *args, **kwargs):
        # print("reorder_levels")
        return self._overload('reorder_levels', *args, **kwargs)

    def repeat(self, *args, **kwargs):
        # print("repeat")
        return self._overload('repeat', *args, **kwargs)

    def replace(self, *args, **kwargs):
        # print("replace")
        return self._overload('replace', *args, **kwargs)

    def resample(self, *args, **kwargs):
        # print("resample")
        return self._overload('resample', *args, **kwargs)

    def reset_index(self, *args, **kwargs):
        # print("reset_index")
        return self._overload('reset_index', *args, **kwargs)

    def rfloordiv(self, *args, **kwargs):
        # print("rfloordiv")
        return self._overload('rfloordiv', *args, **kwargs)

    def rmod(self, *args, **kwargs):
        # print("rmod")
        return self._overload('rmod', *args, **kwargs)

    def rmul(self, *args, **kwargs):
        # print("rmul")
        return self._overload('rmul', *args, **kwargs)

    def rolling(self, *args, **kwargs):
        # print("rolling")
        return self._overload('rolling', *args, **kwargs)

    def round(self, *args, **kwargs):
        # print("round")
        return self._overload('round', *args, **kwargs)

    def rpow(self, *args, **kwargs):
        # print("rpow")
        return self._overload('rpow', *args, **kwargs)

    def rsub(self, *args, **kwargs):
        # print("rsub")
        return self._overload('rsub', *args, **kwargs)

    def rtruediv(self, *args, **kwargs):
        # print("rtruediv")
        return self._overload('rtruediv', *args, **kwargs)

    def sample(self, *args, **kwargs):
        # print("sample")
        return self._overload('sample', *args, **kwargs)

    def searchsorted(self, *args, **kwargs):
        # print("searchsorted")
        return self._overload('searchsorted', *args, **kwargs)

    def select(self, *args, **kwargs):
        # print("select")
        return self._overload('select', *args, **kwargs)

    def sem(self, *args, **kwargs):
        # print("sem")
        return self._overload('sem', *args, **kwargs)

    def set_axis(self, *args, **kwargs):
        # print("set_axis")
        return self._overload('set_axis', *args, **kwargs)

    def shape(self, *args, **kwargs):
        # print("shape")
        return self._overload('shape', *args, **kwargs)

    def shift(self, *args, **kwargs):
        # print("shift")
        return self._overload('shift', *args, **kwargs)

    def size(self, *args, **kwargs):
        # print("size")
        return self._overload('size', *args, **kwargs)

    def skew(self, *args, **kwargs):
        # print("skew")
        return self._overload('skew', *args, **kwargs)

    def slice_shift(self, *args, **kwargs):
        # print("slice_shift")
        return self._overload('slice_shift', *args, **kwargs)

    def sort_index(self, *args, **kwargs):
        # print("sort_index")
        return self._overload('sort_index', *args, **kwargs)

    def sort_values(self, *args, **kwargs):
        # print("sort_values")
        return self._overload('sort_values', *args, **kwargs)

    def squeeze(self, *args, **kwargs):
        # print("squeeze")
        return self._overload('squeeze', *args, **kwargs)

    def std(self, *args, **kwargs):
        # print("std")
        return self._overload('std', *args, **kwargs)

    def strides(self, *args, **kwargs):
        # print("strides")
        return self._overload('strides', *args, **kwargs)

    def sub(self, *args, **kwargs):
        # print("sub")
        return self._overload('sub', *args, **kwargs)

    def subtract(self, *args, **kwargs):
        # print("subtract")
        return self._overload('subtract', *args, **kwargs)

    def sum(self, *args, **kwargs):
        # print("sum")
        return self._overload('sum', *args, **kwargs)

    def swapaxes(self, *args, **kwargs):
        # print("swapaxes")
        return self._overload('swapaxes', *args, **kwargs)

    def swaplevel(self, *args, **kwargs):
        # print("swaplevel")
        return self._overload('swaplevel', *args, **kwargs)

    def tail(self, *args, **kwargs):
        # print("tail")
        return self._overload('tail', *args, **kwargs)

    def take(self, *args, **kwargs):
        # print("take")
        return self._overload('take', *args, **kwargs)

    def timetuple(self, *args, **kwargs):
        # print("timetuple")
        return self._overload('timetuple', *args, **kwargs)

    def to_clipboard(self, *args, **kwargs):
        # print("to_clipboard")
        return self._overload('to_clipboard', *args, **kwargs)

    def to_csv(self, *args, **kwargs):
        # print("to_csv")
        return self._overload('to_csv', *args, **kwargs)

    def to_dense(self, *args, **kwargs):
        # print("to_dense")
        return self._overload('to_dense', *args, **kwargs)

    def to_dict(self, *args, **kwargs):
        # print("to_dict")
        return self._overload('to_dict', *args, **kwargs)

    def to_excel(self, *args, **kwargs):
        # print("to_excel")
        return self._overload('to_excel', *args, **kwargs)

    def to_frame(self, *args, **kwargs):
        # print("to_frame")
        return self._overload('to_frame', *args, **kwargs)

    def to_hdf(self, *args, **kwargs):
        # print("to_hdf")
        return self._overload('to_hdf', *args, **kwargs)

    def to_json(self, *args, **kwargs):
        # print("to_json")
        return self._overload('to_json', *args, **kwargs)

    def to_latex(self, *args, **kwargs):
        # print("to_latex")
        return self._overload('to_latex', *args, **kwargs)

    def to_list(self, *args, **kwargs):
        # print("to_list")
        return self._overload('to_list', *args, **kwargs)

    def to_msgpack(self, *args, **kwargs):
        # print("to_msgpack")
        return self._overload('to_msgpack', *args, **kwargs)

    def to_numpy(self, *args, **kwargs):
        # print("to_numpy")
        return self._overload('to_numpy', *args, **kwargs)

    def to_period(self, *args, **kwargs):
        # print("to_period")
        return self._overload('to_period', *args, **kwargs)

    def to_pickle(self, *args, **kwargs):
        # print("to_pickle")
        return self._overload('to_pickle', *args, **kwargs)

    def to_sparse(self, *args, **kwargs):
        # print("to_sparse")
        return self._overload('to_sparse', *args, **kwargs)

    def to_sql(self, *args, **kwargs):
        # print("to_sql")
        return self._overload('to_sql', *args, **kwargs)

    def to_string(self, *args, **kwargs):
        # print("to_string")
        return self._overload('to_string', *args, **kwargs)

    def to_timestamp(self, *args, **kwargs):
        # print("to_timestamp")
        return self._overload('to_timestamp', *args, **kwargs)

    def to_xarray(self, *args, **kwargs):
        # print("to_xarray")
        return self._overload('to_xarray', *args, **kwargs)

    def transform(self, *args, **kwargs):
        # print("transform")
        return self._overload('transform', *args, **kwargs)

    def transpose(self, *args, **kwargs):
        # print("transpose")
        return self._overload('transpose', *args, **kwargs)

    def truediv(self, *args, **kwargs):
        # print("truediv")
        return self._overload('truediv', *args, **kwargs)

    def truncate(self, *args, **kwargs):
        # print("truncate")
        return self._overload('truncate', *args, **kwargs)

    def tshift(self, *args, **kwargs):
        # print("tshift")
        return self._overload('tshift', *args, **kwargs)

    def tz_convert(self, *args, **kwargs):
        # print("tz_convert")
        return self._overload('tz_convert', *args, **kwargs)

    def tz_localize(self, *args, **kwargs):
        # print("tz_localize")
        return self._overload('tz_localize', *args, **kwargs)

    def unique(self, *args, **kwargs):
        # print("unique")
        return self._overload('unique', *args, **kwargs)

    def unstack(self, *args, **kwargs):
        # print("unstack")
        return self._overload('unstack', *args, **kwargs)

    def update(self, *args, **kwargs):
        # print("update")
        return self._overload('update', *args, **kwargs)

    def value_counts(self, *args, **kwargs):
        # print("value_counts")
        return self._overload('value_counts', *args, **kwargs)

    def values(self, *args, **kwargs):
        # print("values")
        return self._overload('values', *args, **kwargs)

    def var(self, *args, **kwargs):
        # print("var")
        return self._overload('var', *args, **kwargs)

    def view(self, *args, **kwargs):
        # print("view")
        return self._overload('view', *args, **kwargs)

    def where(self, *args, **kwargs):
        # print("where")
        return self._overload('where', *args, **kwargs)

    def xs(self, *args, **kwargs):
        # print("xs")
        return self._overload('xs', *args, **kwargs)