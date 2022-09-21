from typing import List, Union

from pychoco import backend
from pychoco._internals._finite_automaton import _FiniteAutomaton
from pychoco._internals._handle_wrapper import _HandleWrapper
from pychoco._internals._intvar import _IntVar
from pychoco._internals._utils import make_int_3d_array, make_int_2d_array
from pychoco._internals._utils import make_intvar_array, make_int_4d_array
from pychoco.objects.automaton.cost_automaton import CostAutomaton


class _CostAutomaton(_FiniteAutomaton, CostAutomaton, _HandleWrapper):

    def add_counter_state(self, layer_value_state: List[List[List[int]]], min_bound: int, max_bound: int):
        layer_value_state_handle = make_int_3d_array(layer_value_state)
        counter_handle = backend.create_counter_state(layer_value_state_handle, min_bound, max_bound)
        backend.cost_fa_add_counter(self.handle, counter_handle)


def _create_cost_automaton(automaton: Union[_FiniteAutomaton, None] = None):
    if automaton is None:
        handle = backend.create_cost_fa()
    else:
        handle = backend.create_cost_fa_from_fa(automaton.handle)
    return _CostAutomaton(handle)


def _make_single_resource(automaton: _FiniteAutomaton, costs: Union[List[List[int]], List[List[List[int]]]], inf: int,
                          sup: int):
    """
    :param automaton: A finite automaton.
    :param costs: Costs (2 or 3 dimensional int matrix).
    :param inf: Lower bound.
    :param sup: Upper bound.
    :return: A cost automaton from a finite automaton and costs.
    """
    assert len(costs) > 0
    c1 = costs[0]
    assert len(c1) > 0
    c2 = c1[0]
    if isinstance(c2, list):
        assert len(c2) > 0
        handle = backend.make_single_resource_iii(automaton.handle, make_int_3d_array(costs), inf, sup)
    else:
        handle = backend.make_single_resource_ii(automaton.handle, make_int_2d_array(costs), inf, sup)
    return _CostAutomaton(handle)


def _make_multi_resources(automaton: _FiniteAutomaton, costs: Union[List[List[List[int]]], List[List[List[List[int]]]]],
                          bounds: List[_IntVar]):
    assert len(costs) > 0
    c1 = costs[0]
    assert len(c1) > 0
    c2 = c1[0]
    assert len(c2) > 0
    c3 = c2[0]
    if isinstance(c3, list):
        assert len(c3) > 0
        handle = backend.make_multi_resources_iiii(automaton.handle, make_int_4d_array(costs),
                                                   make_intvar_array(bounds))
    else:
        handle = backend.make_multi_resources_iii(automaton.handle, make_int_3d_array(costs),
                                                  make_intvar_array(bounds))
    return _CostAutomaton(handle)
