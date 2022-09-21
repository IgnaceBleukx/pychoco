from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from pychoco import IntVar
from pychoco import backend
from pychoco._internals._handle_wrapper import _HandleWrapper
from pychoco._internals._utils import make_intvar_array, make_int_2d_array


class MultivaluedDecisionDiagram(_HandleWrapper):
    """
    Multi-valued Decision Diagram (MDD)
    """

    def __init__(self, intvars: List["IntVar"], tuples: List[List[int]], compact_once=True, sort_tuple=False):
        """
        Create a MDD

        :param intvars: A list of IntVars.
        :param tuples: A List[List[int]] either tuples (allowed).
        :param compact_once: A bool.
        :param sort_tuple: A bool.
        :return: A MDD.
        """
        assert len(tuples) > 0
        for r in tuples:
            assert len(r) == len(intvars)
        handle = backend.create_mdd_tuples(
            make_intvar_array(intvars),
            make_int_2d_array(tuples),
            compact_once,
            sort_tuple
        )
        super().__init__(handle)
