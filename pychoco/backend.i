%module backend

%{
#define SWIG_FILE_WITH_INIT
#include "backend.h"
%}


%include <typemaps.i>

// custom typemap to append void** types to the result
%typemap(in,numinputs=0,noblock=1) void **OUTPUT ($*1_ltype temp) {
    $1 = &temp;
}

%typemap(argout,noblock=1) void **OUTPUT {
    %append_output(SWIG_NewPointerObj(*$1, $*1_descriptor, SWIG_POINTER_NOSHADOW | %newpointer_flags));
}

%typemap(in,numinputs=0,noblock=1) char **OUTPUT ($*1_ltype temp) {
    $1 = &temp;
}

%typemap(argout,noblock=1) char **OUTPUT {
    %append_output(SWIG_FromCharPtr(($*1_ltype)*$1));
}

// convert a long to a void function pointer
%typemap(in) void *LONG_TO_FPTR { 
    $1 = PyLong_AsVoidPtr($input);    
}

// convert bytearray to c-string
%typemap(in) char *BYTEARRAY {
    if ($input != Py_None) { 
        if (!PyByteArray_Check($input)) {
            SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument "
                       "$argnum"" of type '" "$type""'");
        }
        $1 = (char*) PyByteArray_AsString($input);
    } else { 
        $1 = (char*) 0;
    }
}

// library init

void chocosolver_init();

void chocosolver_cleanup();

int chocosolver_is_initialized();

// Model API

void* create_model();

void* create_model_s(char*);

char* get_model_name(void*);

void* get_solver(void*);

// Solver API

int solve(void*, void*);

void* find_solution(void*, void*);

void* find_all_solutions(void*, void*);

void* find_optimal_solution(void*, void*, int, void*);

void* find_all_optimal_solutions(void*, void*, int, void*);

void show_statistics(void*);

void show_short_statistics(void*);

long get_solution_count(void*);

// Criterion API

void* time_counter(void*, long);

void* solution_counter(void*, long);

void* node_counter(void*, long);

void* fail_counter(void*, long);

void* restart_counter(void*, long);

void* backtrack_counter(void*, long);

// Solution API

int get_int_val(void*, void*);

// Variable (generic)

char* get_variable_name(void*);

int is_instantiated(void*);

// Intvars

void* intvar_sii(void*, char*, int, int);

void* intvar_ii(void*, int, int);

void* intvar_i(void*, int);

void* intvar_si(void*, char*, int);

char* get_intvar_name(void*);

int get_intvar_lb(void*);

int get_intvar_ub(void*);

int get_intvar_value(void*);

// Boolvars

void* boolvar_s(void*, char*);

void* boolvar(void*);

void* boolvar_b(void*, int);

void* boolvar_sb(void*, char*, int);

// Constraints

char* get_constraint_name(void*);

void post(void*);

void* reify(void*);

int is_satisfied(void*);

void* arithm_iv_cst(void*, void*, char*, int);

void* arithm_iv_iv(void*, void*, char*, void*);

void* arithm_iv_iv_cst(void*, void*, char*, void*, char*, int);

void* arithm_iv_iv_iv(void*, void*, char*, void*, char*, void*);

void* member_iv_iarray(void*, void*, void*);

void* member_iv_i_i(void*, void*, int, int);

void* mod_iv_i_i(void*, void*, int, int);

void* mod_iv_i_iv(void*, void*, int, void*);

void* mod_iv_iv_iv(void*, void*, void*, void*);

void* not_(void*, void*);

void* not_member_iv_iarray(void*, void*, void*);

void* not_member_iv_i_i(void*, void*, int, int);

void* absolute(void*, void*, void*);

void* distance_iv_iv_i(void*, void*, void*, char*, int);

void* distance_iv_iv_iv(void*, void*, void*, char*, void*);

void* element_iv_iarray_iv_i(void*, void*, void*, void*, int);

void* element_iv_ivarray_iv_i(void*, void*, void*, void*, int);

void* square(void*, void*, void*);

void* times_iv_i_iv(void*, void*, int, void*);

void* times_iv_iv_i(void*, void*, void*, int);

void* times_iv_iv_iv(void*, void*, void*, void*);

void* div_(void*, void*, void*, void*);

void* max_iv_iv_iv(void*, void*, void*, void*);

void* max_iv_ivarray(void*, void*, void*);

void* min_iv_iv_iv(void*, void*, void*, void*);

void* min_iv_ivarray(void*, void*, void*);

void* all_different(void*, void*);

void* all_equal(void*, void*);

void* not_all_equal(void*, void*);

void* among(void*, void*, void*, void*);

void* and_bv_bv(void*, void*);

void* and_cs_cs(void*, void*);

void* at_least_n_values(void*, void*, void*, int);

void* at_most_n_values(void*, void*, void*, int);

void* bin_packing(void*, void*, void*, void*, int);

void* bools_int_channeling(void*, void*, void*, int);

void* bits_int_channeling(void*, void*, void*);

void* clauses_int_channeling(void*, void*, void*, void*);

void* circuit(void*, void*, int, char*);

void* count_i(void*, int, void*, void*);

void* count_iv(void*, void*, void*, void*);

void* diff_n(void*, void*, void*, void*, void*, int);

void* global_cardinality(void*, void*, void*, void*, int);

void* inverse_channeling(void*, void*, void*, int, int, int);

void* int_value_precede_chain(void*, void*, void*);

void* knapsack(void*, void*, void*, void*, void*, void*);

void* lex_chain_less(void*, void*);

void* lex_chain_less_eq(void*, void*);

void* lex_less(void*, void*, void*);

void* lex_less_eq(void*, void*, void*);

void* argmax(void*, void*, int, void*);

void* argmin(void*, void*, int, void*);

void* n_values(void*, void*, void*);

void* or_bv_bv(void*, void*);

void* or_cs_cs(void*, void*);

void* path(void*, void*, void*, void*, int);

void* scalar_i(void*, void*, void*, char*, int);

void* scalar_iv(void*, void*, void*, char*, void*);

void* sort(void*, void*, void*);

void* sub_circuit(void*, void*, int, void*);

void* sub_path(void*, void*, void*, void*, int, void*);

void* sum_iv_i(void*, void*, char*, int);

void* sum_iv_iv(void*, void*, char*, void*);

void* sum_ivarray_ivarray(void*, void*, char*, void*);

void* sum_bv_i(void*, void*, char*, int);

void* sum_bv_iv(void*, void*, char*, void*);

void* tree(void*, void*, void*, int);

// Array API

// IntVar

void* create_intvar_array(int);

int intvar_array_length(void*);

void intvar_array_set(void*, void*, int);

// BoolVar

void* create_boolvar_array(int);

void boolvar_array_set(void*, void*, int);

// Constraint

void* create_constraint_array(int);

void constraint_array_set(void*, void*, int);

// int

void* create_int_array(int);

int int_array_length(void*);

void int_array_set(void*, int, int);

// Criterion

void* create_criterion_array(int);

void criterion_array_set(void*, void*, int);

int array_length(void*);

// List API

int list_size(void*);

// Solution

void* list_solution_get(void*, int);

// Search

void set_random_search(void*, void*, long);

void set_dom_over_w_deg_search(void*, void*);

void set_dom_over_w_deg_ref_search(void*, void*);

void set_activity_based_search(void*, void*);

void set_min_dom_lb_search(void*, void*);

void set_min_dom_ub_search(void*, void*);

void set_conflict_history_search(void*, void*);

void set_default_search(void*);

void set_input_order_lb_search(void*, void*);

void set_input_order_ub_search(void*, void*);

void set_failure_length_based_search(void*, void*);

void set_failure_rate_based_search(void*, void*);

// Handle API

void chocosolver_handles_destroy(void*);
