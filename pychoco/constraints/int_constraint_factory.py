from abc import ABC, abstractmethod
from typing import Union, List

from pychoco.constraints.constraint import Constraint
from pychoco.variables.boolvar import BoolVar
from pychoco.variables.intvar import IntVar


class IntConstraintFactory(ABC):
    """
    Factory for constraints over integer variables.
    """

    @abstractmethod
    def arithm(self, x: IntVar, op1: str, y: Union[int, IntVar],
               op2: Union[None, str] = None, z: Union[None, int, IntVar] = None):
        """
        Creates an arithmetic constraint, where operators are in {"=", "!=", ">","<",">=","<="}
        and {"+", "-", "*", "/"}.
        Four options are possible:
            - `x <op1> y`,
                    x -> IntVar; y -> constant; op2 and z -> None.
                    op1 in {"=", "!=", ">","<",">=","<="}
            - `x <op1> y`,
                    x and y -> IntVar; operator3 and z -> None.
                    op1 in {"=", "!=", ">","<",">=","<="}
            - `x <op1> y <op2> z`,
                    x and y -> IntVar, z -> constant.
                    op1 in {"=", "!=", ">","<",">=","<="} and op2 in {"+", "-", "*", "/"}, or vice-versa.
            - `x <op1> y <op2> z`,
                    x, y, and z -> IntVar.
                    op1 in {"=", "!=", ">","<",">=","<="} and op2 in {"+", "-", "*", "/"}, or vice-versa.
        :param x: An IntVar object.
        :param op1: An str in {"=", "!=", ">","<",">=","<="} or {"+", "-", "*", "/"}.
        :param y: An IntVar object or a constant (integer).
        :param op2: An str in {"=", "!=", ">","<",">=","<="} or {"+", "-", "*", "/"}, or None.
        :param z: An IntVar object, a constant (integer), or None.
        :return: An arithmetic constraint.
        """
        pass

    @abstractmethod
    def member(self, x: IntVar, table: Union[list, tuple, None] = None,
               lb: Union[None, int] = None, ub: Union[None, int] = None):
        """
        Creates a member constraint. Ensures `x` takes its values in `table`, or in [`lb`, `ub`].
        If `table` is not `None`, the first option is applied, otherwise `lb` and `ub` must not be `None`.
        :param x: An `IntVar`.
        :param table: A list of integers, or `None`.
        :param lb: An integer, or `None`.
        :param ub: An integer, or `None`.
        :return: A member constraint.
        """
        pass

    @abstractmethod
    def not_member(self, x: IntVar, table: Union[list, tuple, None] = None,
                   lb: Union[None, int] = None, ub: Union[None, int] = None):
        """
        Creates a not_member constraint. Ensures `x` does not take its values in `table`, or in [`lb`, `ub`].
        If `table` is not `None`, the first option is applied, otherwise `lb` and `ub` must not be `None`.
        :param x: An `IntVar`.
        :param table: A list of integers, or `None`.
        :param lb: An integer, or `None`.
        :param ub: An integer, or `None`.
        :return: A not_member constraint.
        """
        pass

    @abstractmethod
    def all_different(self, *intvars: List[IntVar]):
        """
        Creates an allDifferent constraint, which ensures that all variables from vars take a different value.
        :param intvars: A list of integer variables.
        :return: An allDifferent constraint.
        """
        pass

    @abstractmethod
    def mod(self, x, mod: Union[int, IntVar], res: Union[int, IntVar]):
        """
        Creates a modulo constraint. Ensures X % mod = res.
        If mod is an `IntVar`, the constraint uses truncated division: the quotient is defined by truncation
        q = trunc(a/n) and the remainder would have same sign as the dividend. The quotient is rounded towards
        zero: equal to the first integer in the direction of zero from the exact rational quotient.
        :param x: An `IntVar`.
        :param mod: A constant (int), or an `IntVar`.
        :param res: A constant (int), or an `IntVar`.
        :return: A modulo constraint.
        """
        pass

    @abstractmethod
    def not_(self, constraint: Constraint):
        """
        Gets the opposite of a given constraint.
        Works for any constraint, including globals, but the associated performances might be weak.
        :param constraint: A constraint.
        :return: A not constraint.
        """
        pass

    @abstractmethod
    def absolute(self, x: IntVar, y: IntVar):
        """
        Creates an absolute value constraint: x = |y|.
        :param x: An IntVar.
        :param y: An IntVar.
        :return: An absolute constraint.
        """
        pass

    @abstractmethod
    def distance(self, x: IntVar, y: IntVar, op: str, z: Union[int, IntVar]):
        """
        Creates a distance constraint : |x-y| op z,
        where op can take its value among:
            - {"=", ">", "<", "!="} if z is a constant
            - {"=", ">", "<"} if z is an IntVar
        :param x: An IntVar.
        :param y: An IntVar.
        :param op: An operator (str), which can take its value among {"=", ">", "<", "!="} if z is a constant or
                   {"=", ">", "<"} if z is an IntVar.
        :param z: An IntVar or a constant (int).
        :return: A distance constraint.
        """
        pass

    @abstractmethod
    def element(self, x: IntVar, table: Union[List[int], List[IntVar]], index: IntVar, offset: int = 0):
        """
        Creates an element constraint: x = table[index-offset]
        where table is a list of variables or integers.
        :param x: An IntVar.
        :param table: A list of IntVars or a list of integers.
        :param index: An IntVar.
        :param offset: An integer.
        :return: An element constraint.
        """
        pass

    @abstractmethod
    def square(self, x: IntVar, y: IntVar):
        """
        Creates a square constraint: x = y^2.
        :param x: An IntVar.
        :param y: An IntVar.
        :return: A square constraint.
        """
        pass

    @abstractmethod
    def times(self, x: IntVar, y: Union[int, IntVar], z: Union[int, IntVar]):
        """
        Creates a multiplication constraint: x * y = z.
        :param x: An IntVar.
        :param y: An IntVar or an int.
        :param z: An IntVar or an int.
        :return: A times constraint.
        """
        pass

    @abstractmethod
    def div(self, dividend: IntVar, divisor: IntVar, result: IntVar):
        """
        Creates a euclidean division constraint. Ensures dividend / divisor = result, rounding towards 0.
        Also ensures divisor != 0
        :param dividend: An IntVar.
        :param divisor: An IntVar.
        :param result: An IntVar.
        :return: A div constraint.
        """
        pass

    @abstractmethod
    def max(self, x: IntVar, *intvars: List[IntVar]):
        """
        Creates a maximum constraint, x is the maximum value among IntVars in *intvars.
        :param x: An IntVar.
        :param intvars: A list of IntVars.
        :return: A max constraint.
        """
        pass

    @abstractmethod
    def min(self, x: IntVar, *intvars: List[IntVar]):
        """
        Creates a minimum constraint, x is the minimum value among IntVars in *intvars.
        :param x: An IntVar.
        :param intvars: A list of IntVars.
        :return: A min constraint.
        """
        pass

    # TODO Test from here

    @abstractmethod
    def all_equal(self, *intvars: List[IntVar]):
        """
        Creates an all_equal constraint.
        Ensures that all variables from vars take the same value
        :param intvars: A list of IntVars.
        :return: An all_equal constraint.
        """
        pass

    @abstractmethod
    def not_all_equal(self, *intvars: List[IntVar]):
        """
        Creates a not_all_equal constraint.
        Ensures that not all variables from vars take the same value
        :param intvars: A list of IntVars.
        :return: A not_all_equal constraint.
        """
        pass

    @abstractmethod
    def among(self, nb_var: IntVar, intvars: List[IntVar], values: List[int]):
        """
        Creates an among constraint.
        `nb_var` is the number of variables of the collection `intvars` that take their value in `values`.
        Propagator :
        C. Bessiere, E. Hebrard, B. Hnich, Z. Kiziltan, T. Walsh,
        Among, common and disjoint Constraints
        CP-2005
        :param nb_var: An IntVar.
        :param intvars: A list of IntVars.
        :param values: A list of ints.
        :return: An among constraint.
        """
        pass

    @abstractmethod
    def and_(self, *bools_or_constraints: Union[List[BoolVar], List[Constraint]]):
        """
        Creates an and constraint that is satisfied if all boolean variables or constraint in
        `bools_or_constraints` are respectively true or satisfied.
        :param bools_or_constraints: Either a list of BoolVars or a list of Constraints.
        :return: An and constraint.
        """
        pass

    @abstractmethod
    def at_least_n_values(self, intvars: List[IntVar], n_values: IntVar, ac: bool = False):
        """
        Creates an at_least_n_value constraint.
        Let N be the number of distinct values assigned to the variables of the intvars collection.
        Enforce condition N >= n_values to hold.
        This embeds a light propagator by default.
        Additional filtering algorithms can be added.
        :param intvars: list of IntVars.
        :param n_values: IntVar (limit variable).
        :param ac: If True, add additional filtering algorithm, domain filtering algorithm derivated
                   from (Soft) AllDifferent.
        :return: An at_least_n_values constraint.
        """
        pass

    @abstractmethod
    def at_most_n_values(self, intvars: List[IntVar], n_values: IntVar, strong: bool = False):
        """
        Creates an at_mostn_value constraint.
        Let N be the number of distinct values assigned to the variables of the intvars collection.
        Enforce condition N <= n_values to hold.
        This embeds a light propagator by default.
        Additional filtering algorithms can be added.
        :param intvars: list of IntVars.
        :param n_values: IntVar (limit variable).
        :param strong: "AMNV<Gci|MDRk|R13>" Filters the conjunction of AtMostNValue and inequalities
                       (see Fages and Lap&egrave;gue Artificial Intelligence 2014)
                       automatically detects inequalities and allDifferent constraints.
                       Presumably useful when nValues must be minimized.
        :return: An at_most_n_values constraint.
        """
        pass

    @abstractmethod
    def bin_packing(self, item_bin: List[IntVar], item_size: List[int], bin_load: List[IntVar], offset: int = 0):
        """
        Creates a bin_packing constraint.
        Bin Packing formulation:
        forall b in [0, bin_load.length - 1],
        bin_load[b] = sum(item_size[i] | i in [0,item_size.length-1], item_bin[i] = b + offset
        forall i in [0, item_size.length - 1], item_bin is in [offset, bin_load.length-1 + offset].
        :param item_bin: IntVars representing the bin of each item.
        :param item_size: ints representing the size of each item.
        :param bin_load: IntVars representing the load of each bin (i.e. the sum of the size of the items in it).
        :param offset: 0 by default but typically 1 if used within MiniZinc
                       (which counts from 1 to n instead of from 0 to n-1)
        :return: A bin_packing constraint.
        """
        pass

    @abstractmethod
    def bools_int_channeling(self, boolvars: List[BoolVar], intvar: IntVar, offset: int = 0):
        """
        Creates a channeling constraint between an integer variable and a set of boolean variables.
        Maps the boolean assignments variables boolvars with the standard assignment variable intvar.
        intvar = i <-> boolvars[i - offset] = 1
        :param boolvars: A list of BoolVars.
        :param intvar: An IntVar.
        :param offset: 0 by default but typically 1 if used within MiniZinc
                       which counts from 1 to n instead of from 0 to n-1.
        :return: A bools_int_channeling constraint.
        """
        pass

    @abstractmethod
    def bits_int_channeling(self, bits: List[BoolVar], intvar: IntVar):
        """
        Creates a channeling constraint between an integer variable and a set of bit variables.
        Ensures that intvar = 2<sup>0</sup>*BIT_1 + 2<sup>1</sup>*BIT_2 + ... 2<sup>n-1</sup>*BIT_n.
        BIT_1 is related to the first bit of OCTET (2^0),
        BIT_2 is related to the first bit of OCTET (2^1), etc.
        The upper bound of intvar is given by 2<sup>n</sup>, where n is the size of the array bits.
        :param bits: A list of BoolVars.
        :param intvar: An IntVar.
        :return: A bits_int_channeling constraint.
        """
        pass

    @abstractmethod
    def clauses_int_channeling(self, intvar: IntVar, e_vars: List[BoolVar], l_vars: List[BoolVar]):
        """
        Creates a channeling constraint between an integer variable and a set of clauses.
        Link each value from the domain of intvar to two boolean variable:
        one reifies the equality to the i^th value of the variable domain,
        the other reifies the less-or-equality to the i^th value of the variable domain.
        Contract: e_vars.lenght == l_vars.length == intvar.getUB() - intvar.getLB() + 1
        Contract: intvar is not a boolean variable
        :param intvar: An IntVar.
        :param e_vars: A list of EQ BoolVars.
        :param l_vars: A list of LEQ BoolVars.
        :return: A clauses_int_channeling constraint.
        """
        pass

    @abstractmethod
    def circuit(self, intvars: List[IntVar], offset: int = 0, conf: str = "RD"):
        """
        Creates a circuit constraint which ensures that
        the elements of intvars define a covering circuit
        where intvars[i] = offset + j means that j is the successor of i.
        Filtering algorithms:
        - subtour elimination : Caseau & Laburthe (ICLP'97)
        - allDifferent GAC algorithm: R&eacute;gin (AAAI'94)
        - dominator-based filtering: Fages & Lorca (CP'11)
        - Strongly Connected Components based filtering (Cambazard & Bourreau JFPC'06 and Fages and Lorca TechReport'12)
        See Fages PhD Thesis (2014) for more information.
        :param intvars: A list of IntVars.
        :param offset: 0 by default but typically 1 if used within MiniZinc
                       (which counts from 1 to n instead of from 0 to n-1).
        :param conf: Filtering options, among ["LIGHT", "FIRST", "RD", and "ALL"].
        :return: A circuit constraint.
        """
        pass

    @abstractmethod
    def count(self, value: Union[int, IntVar], intvars: List[IntVar], limit: IntVar):
        """
        Creates a count constraint.
        Let N be the number of variables of the intvars collection assigned to value `value`;
        Enforce condition N = limit to hold.
        :param value: An int.
        :param intvars: A list of IntVars.
        :param limit: An int or an IntVar.
        :return: A count constraint.
        """
        pass

    @abstractmethod
    def diff_n(self, x: List[IntVar], y: List[IntVar], width: List[IntVar], height: List[IntVar],
               add_cumulative_reasoning: bool = True):
        """
        Creates a diff_n constraint. Constrains each rectangle<sub>i</sub>, given by their origins x<sub>i</sub>,y<sub>i</sub>
        and sizes width<sub>i</sub>,height<sub>i</sub>, to be non-overlapping.
        :param x: A list of IntVars.
        :param y: A list of IntVars.
        :param width: A list of IntVars.
        :param height: A list of IntVars.
        :param add_cumulative_reasoning: Indicates whether redundant cumulative constraints should be put
                                         on each dimension or not (advised).
        :return: A diff_n constraint.
        """
        pass

    @abstractmethod
    def global_cardinality(self, intvars: List[IntVar], values: List[int], occurrences: List[IntVar],
                           closed: bool = False):
        """
        Creates a global cardinality constraint (GCC):
        Each value values[i] should be taken by exactly occurrences[i] variables of intvars.
        This constraint does not ensure any well-defined level of consistency, yet.
        :param intvars: A list of IntVars.
        :param values: A list of ints.
        :param occurrences: A list of IntVars.
        :param closed: If True, restricts domains of intvars to values.
        :return: A global_cardinality constraint.
        """
        pass

    @abstractmethod
    def inverse_channeling(self, intvars1: List[IntVar], intvars2: List[IntVar], offset1: int = 0,
                           offset2: int = 0, ac: bool = False):
        """
        Creates an inverse channeling between vars1 and vars2:
        intvars1[i - offset2] = j <=> intvars2[j - offset1] = i
        Performs AC if domains are enumerated.
        If not, then it works on bounds without guaranteeing BC.
        (enumerated domains are strongly recommended).
        beware you should have |intvars1| = |intvars2|.
        :param intvars1: A list of IntVars.
        :param intvars2: A list of IntVars.
        :param offset1: an int.
        :param offset2: an int.
        :param ac: A bool.
        :return: An inverse_channeling constraint.
        """
        pass

    @abstractmethod
    def int_value_precede_chain(self, intvars: List[IntVar], *values: List[int]):
        """
        Creates an int_value_precede_chain constraint.
        Ensure that, for each pair of values[k] and values[l], such that k < l,
        if there exists <code>j</code> such that intvars[j] = intvars[l], then, there must exist
        <code>i</code> <<code>j</code> such that intvars[i] = intvars[k].
        :param intvars: A list of IntVars.
        :param values: A list of distinct ints.
        :return: An int_value_precede_chain constraint.
        """
        pass

    @abstractmethod
    def knapsack(self, occurrences: List[IntVar], weight_sum: IntVar, energy_sum: IntVar, weight: List[int],
                 energy: List[int]):
        """
        Creates a knapsack constraint.
        Ensures that :
        <br/>- occurrences[i] * weight[i] = weight_sum
        <br/>- occurrences[i] * energy[i] = energy_sum
        <br/>and maximizing the value of energy_sum.
        A knapsack constraint
        <a href="http://en.wikipedia.org/wiki/Knapsack_problem">wikipedia</a>:<br/>
        "Given a set of items, each with a weight and an energy value,
        determine the count of each item to include in a collection so that
        the total weight is less than or equal to a given limit and the total value is as large as possible.
        It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack
        and must fill it with the most useful items."
        The limit over weightSum has to be specified either in its domain or with an additional constraint:
        <pre>
            model.arithm(weight_sum, "<=", limit).post()
        </pre>
        :param occurrences: A list of IntVars.
        :param weight_sum: An IntVar.
        :param energy_sum: An IntVar.
        :param weight: A list of ints.
        :param energy: A list of ints.
        :return: A knapsack constraint.
        """
        pass

    @abstractmethod
    def lex_chain_less(self, *intvars: List[IntVar]):
        """
        Creates a lex_chain_less constraint.
        For each pair of consecutive vectors intvars<sub>i</sub> and intvars<sub>i+1</sub> of the intvars collection
        intvars<sub>i</sub> is lexicographically strictly less than intvars<sub>i+1</sub>
        :param intvars: A list of IntVars.
        :return: A lex_chain_less constraint.
        """
        pass

    @abstractmethod
    def lex_chain_less_eq(self, *intvars: List[IntVar]):
        """
        Creates a lex_chain_less_eq constraint.
        For each pair of consecutive vectors intvars<sub>i</sub> and intvars<sub>i+1</sub> of the intvars collection
        intvars<sub>i</sub> is lexicographically less or equal than intvars<sub>i+1</sub>
        :param intvars: A list of IntVars.
        :return: A lex_chain_less_eq constraint.
        """
        pass

    @abstractmethod
    def lex_less(self, intvars1: List[IntVar], intvars2: List[IntVar]):
        """
        Creates a lex_less constraint.
        Ensures that intvars1 is lexicographically strictly less than intvars2.
        :param intvars1: A list of IntVars.
        :param intvars2: A list of IntVars.
        :return: A lex_less constraint.
        """
        pass

    @abstractmethod
    def lex_less_eq(self, intvars1: List[IntVar], intvars2: List[IntVar]):
        """
        Creates a lex_less_eq constraint.
        Ensures that intvars1 is lexicographically strictly less or equal than intvars2.
        :param intvars1: A list of IntVars.
        :param intvars2: A list of IntVars.
        :return: A lex_less_eq constraint.
        """
        pass

    @abstractmethod
    def argmax(self, intvar: IntVar, offset: int, intvars: List[IntVar]):
        """
        Creates an argmax constraint.
        intvar is the index of the maximum value of the collection of domain variables intvars.
        :param intvar: An IntVar.
        :param offset: an int.
        :param intvars: A list of IntVars.
        :return: An argmax constraint.
        """
        pass

    @abstractmethod
    def argmin(self, intvar: IntVar, offset: int, intvars: List[IntVar]):
        """
        Creates an argmin constraint.
        intvar is the index of the minimum value of the collection of domain variables intvars.
        :param intvar: An IntVar.
        :param offset: an int.
        :param intvars: A list of IntVars.
        :return: An argmin constraint.
        """
        pass

    @abstractmethod
    def n_values(self, intvars: List[IntVar], n_values: IntVar):
        """
        Creates an n_values constraint.
        Let N be the number of distinct values assigned to the variables of the intvars collection.
        Enforce condition N = n_values to hold.
        :param intvars: A list of IntVars.
        :param n_values: An IntVar.
        :return: An n_values constraint.
        """
        pass

    @abstractmethod
    def or_(self, *bools_or_constraints: Union[List[BoolVar], List[Constraint]]):
        """
        Creates a or constraint that is satisfied if at least one boolean variable or constraint in
        `bools_or_constraints` is respectively true or satisfied.
        :param bools_or_constraints: Either a list of BoolVars or a list of Constraints.
        :return: An or constraint.
        """
        pass

    @abstractmethod
    def path(self, intvars: List[IntVar], start: IntVar, end: IntVar, offset: int = 0):
        """
        Creates a path constraint which ensures that
        <p/> the elements of intvars define a covering path from start to end
        <p/> where intvars[i] = j means that j is the successor of i.
        <p/> Moreover, intvars[end] = |intvars|
        <p/> Requires : |intvars|>0
        Filtering algorithms: see circuit constraint
        :param intvars: A list of IntVars.
        :param start: An IntVar.
        :param end: An IntVar.
        :param offset: An int.
        :return: A path constraint.
        """
        pass

    @abstractmethod
    def scalar(self, intvars: List[IntVar], coeffs: List[int], operator: str, scalar: Union[int, IntVar]):
        """
        Creates a scalar constraint which ensures that Sum(intvars[i] * coeffs[i]) operator scalar.
        :param intvars: A list of IntVars.
        :param coeffs: A list of ints, such that |intvars| = |coeffs|.
        :param operator: A str in ["=", "!=", ">","<",">=","<="].
        :param scalar: An int or an IntVar.
        :return: A scalar constraint.
        """
        pass

    @abstractmethod
    def sort(self, intvars: List[IntVar], sorted_intvars: List[IntVar]):
        """
        Creates a sort constraint which ensures that the variables of sorted_intvars correspond to the variables
        of intvars according to a permutation. The variables of sorted_intvars are also sorted in increasing order.
        For example:
        - X= (4,2,1,3)
        - Y= (1,2,3,4)
        :param intvars: A list of IntVars.
        :param sorted_intvars: A list of IntVars.
        :return: A sort constraint.
        """
        pass

    @abstractmethod
    def sub_circuit(self, intvars: List[IntVar], offset: int, sub_circuit_length: IntVar):
        """
        Creates a sub_circuit constraint which ensures that
        <p/> the elements of intvars define a single circuit of sub_circuit_length nodes where
        <p/> intvars[i] = offset + j means that j is the successor of i.
        <p/> and intvars[i] = offset + i means that i is not part of the circuit
        <p/> the constraint ensures that |{intvars[i] =/= offset + i}| = sub_circuit_length
        <p/> Filtering algorithms:
        <p/> subtour elimination : Caseau & Laburthe (ICLP'97)
        <p/> allDifferent GAC algorithm: R&eacute;gin (AAAI'94)
        <p/> dominator-based filtering: Fages & Lorca (CP'11) (adaptive scheme by default, see implementation)
        :param intvars: A list of IntVars.
        :param offset: An int.
        :param sub_circuit_length: An IntVar.
        :return: A sub_circuit constraint.
        """
        pass

    @abstractmethod
    def sub_path(self, intvars: List[IntVar], start: IntVar, end: IntVar, offset: int, sub_path_length: IntVar):
        """
        Creates a sub_path constraint which ensures that
        <p/> the elements of intvars define a path of sub_path_length vertices, leading from start to end
        <p/> where intvars[i] = offset + j means that j is the successor of i.
        <p/> where intvars[i] = offset + i means that vertex i is excluded from the path.
        <p/> Moreover, intvars[end - offset] = |intvars| + offset
        <p/> Requires : |vars|>0
        Filtering algorithms: see subCircuit constraint
        :param intvars: A list of IntVars.
        :param start: An IntVar.
        :param end: An IntVar.
        :param offset: An int.
        :param sub_path_length: An IntVar.
        :return: A sub_path constraint.
        """
        pass

    @abstractmethod
    def sum(self, intvars_or_boolvars: Union[List[IntVar], List[BoolVar]], operator: str,
            sum_result: Union[int, IntVar, List[IntVar]]):
        """
        Creates a sum constraint.
        Enforces that Sum<sub>i in |intvars_or_boolvars|</sub>intvars_or_boolvars<sub>i</sub> operator sum_result.
        :param intvars_or_boolvars: Either a list of IntVars or a list of BoolVars.
        :param operator: A str in ["=", "!=", ">","<",">=","<="].
        :param sum_result: Either an int, an IntVar, or a list of IntVars.
        :return: A sum constraint.
        """
        pass

    @abstractmethod
    def tree(self, successors: List[IntVar], nb_trees: IntVar, offset: int = 0):
        """
        Creates a tree constraint.
        Partition successors variables into nb_trees (anti) arborescence.
        <p/> successors[i] = offset + j means that j is the successor of i.
        <p/> and successors[i] = offset + i means that i is a root.
        <p/> dominator-based filtering: Fages & Lorca (CP'11).
        <p/> However, the filtering over nbTrees is quite light here.
        :param successors: A list of IntVars.
        :param nb_trees: An IntVar.
        :param offset: An int.
        :return: A tree constraint.
        """
        pass
