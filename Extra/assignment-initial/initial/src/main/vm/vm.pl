% main program

% Kiểm tra giá trị boolean
is_bool(true).
is_bool(false).

% Chương trình chính
reduce_prog([Var, Procs, Body]) :-
    check_redeclarations(Var),
    create_env(Var, env([[]], false, Procs), Env),
    check_procs(Procs, Env),
    reduce_stmt(config(Body, Env), _).

% Kiểm tra khai báo lại
check_redeclarations(Vars) :-
    check_redeclarations(Vars, []).

check_redeclarations([], _).
check_redeclarations([var(X, Type)|Vars], Seen) :-
    (   member(X, Seen) ->
        throw(redeclare_identifier(var(X, Type)))
    ;   is_builtin(X, _) ->
        throw(redeclare_identifier(var(X, Type)))
    ;   check_redeclarations(Vars, [X|Seen])
    ).
check_redeclarations([const(X, Val)|Vars], Seen) :-
    (   member(X, Seen) ->
        throw(redeclare_identifier(const(X, Val)))
    ;   is_builtin(X, _) ->
        throw(redeclare_identifier(const(X, Val)))
    ;   check_redeclarations(Vars, [X|Seen])
    ).

% Kiểm tra khai báo hàm/thủ tục
% check_procs(+Procs, +Env)
% Khởi đầu Seen = []  
check_procs(Procs, Env) :-
    check_procs(Procs, Env, []).

% Khi hết danh sách thì thành công
check_procs([], _, _).

% Hàm
check_procs([func(Name, _, _, _)|Rest], Env, Seen) :-
    (   is_builtin(Name, _) ->
        throw(redeclare_function(Name))
    ;   has_declared(Name, Env, _) ->
        throw(redeclare_function(Name))
    ;   member(Name-_, Seen)  % chỉ kiểm tra Name đã xuất hiện
    ->  throw(redeclare_function(Name))
    ;   check_procs(Rest, Env, [Name-func|Seen])
    ).

% Thủ tục
check_procs([proc(Name, _, _)|Rest], Env, Seen) :-
    (   is_builtin(Name, _) ->
        throw(redeclare_procedure(Name))
    ;   has_declared(Name, Env, _) ->
        throw(redeclare_procedure(Name))
    ;   member(Name-_, Seen)  % nếu Name đã xuất hiện (dù là func hay proc)
    ->  throw(redeclare_procedure(Name))
    ;   check_procs(Rest, Env, [Name-proc|Seen])
    ).

% Kiểm tra khai báo định danh
has_declared(X, env([L|_], _, _), id(X, Kind, Val, Type)) :- member(id(X, Kind, Val, Type), L), !.
has_declared(X, env([_|Rest], LoopFlag, Procs), R) :- has_declared(X, env(Rest, LoopFlag, Procs), R).

% Tạo môi trường
create_env([], L, L).
create_env([var(X, Type)|L], env([L1|L2], T, Procs), L3) :-
    create_env(L, env([[id(X, var, undef, Type)|L1]|L2], T, Procs), L3).
create_env([const(X, Val)|L], env([L1|L2], T, Procs), L3) :-
    create_env(L, env([[id(X, const, Val, unknown)|L1]|L2], T, Procs), L3).

% Giảm biểu thức
reduce(config(add(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        (   (float(V1); float(V2)) -> R is float(V1 + V2) ; R is V1 + V2 )
    ;   throw(type_mismatch(add(E1, E2)))
    ).
reduce(config(sub(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        (   (float(V1); float(V2)) -> R is float(V1 - V2) ; R is V1 - V2 )
    ;   throw(type_mismatch(sub(E1, E2)))
    ).
reduce(config(times(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        (   (float(V1); float(V2)) -> R is float(V1 * V2) ; R is V1 * V2 )
    ;   throw(type_mismatch(times(E1, E2)))
    ).
reduce(config(rdiv(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)), V2 =\= 0 ->
        R is float(V1 / V2)
    ;   throw(type_mismatch(rdiv(E1, E2)))
    ).
reduce(config(idiv(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   integer(V1), integer(V2), V2 =\= 0 ->
        R is V1 div V2
    ;   throw(type_mismatch(idiv(E1, E2)))
    ).
reduce(config(imod(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   integer(V1), integer(V2), V2 =\= 0 ->
        R is V1 mod V2
    ;   throw(type_mismatch(imod(E1, E2)))
    ).
reduce(config(sub(E1), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    (   (integer(V1); float(V1)) ->
        R is -V1
    ;   throw(type_mismatch(sub(E1)))
    ).
reduce(config(bnot(E1), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    (   is_bool(V1) ->
        R is \V1
    ;   throw(type_mismatch(bnot(E1)))
    ).
reduce(config(band(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    (   V1 = false ->
        R = false
    ;   reduce_all(config(E2, Env), config(V2, Env)),
        (   is_bool(V2) ->
            (V2 = false -> R = false ; R = true)
        ;   throw(type_mismatch(band(E1, E2)))
        )
    ).
reduce(config(bor(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    (   V1 = true ->
        R = true
    ;   reduce_all(config(E2, Env), config(V2, Env)),
        (   is_bool(V2) ->
            (V2 = true -> R = true ; R = false)
        ;   throw(type_mismatch(bor(E1, E2)))
        )
    ).
reduce(config(greater(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        R = (V1 > V2)
    ;   throw(type_mismatch(greater(E1, E2)))
    ).

reduce(config(less(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        R = (V1 < V2)
    ;   throw(type_mismatch(less(E1, E2)))
    ).

reduce(config(ge(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        R = (V1 >= V2)
    ;   throw(type_mismatch(ge(E1, E2)))
    ).

reduce(config(le(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1); float(V1)), (integer(V2); float(V2)) ->
        R = (V1 =< V2)
    ;   throw(type_mismatch(le(E1, E2)))
    ).

reduce(config(eq(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1), integer(V2); is_bool(V1), is_bool(V2)) ->
        R = (V1 =:= V2)
    ;   throw(type_mismatch(eq(E1, E2)))
    ).

reduce(config(ne(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1), integer(V2); is_bool(V1), is_bool(V2)) ->
        R = (V1 =\= V2)
    ;   throw(type_mismatch(ne(E1, E2)))
    ).
reduce(config(I, Env), config(V, Env)) :-
    atom(I),
    (   has_declared(I, Env, id(I, _, V, _)) ->
        (   V = undef -> throw(invalid_expression(I)) ; true )
    ;   throw(undeclare_identifier(I))
    ).
reduce(config(call(Name, Args), Env), config(R, Env)) :-
    is_builtin(Name, func),
    reduce_args(Args, Env, Vals),
    p_call_builtin(Name, Vals, R), !.
reduce(config(call(Name, Args), Env), config(R, NewEnv)) :-
    lookup_func(Name, Env, func(Name, Params, _, Stmts)),
    length(Args, N), length(Params, N), !,
    reduce_args(Args, Env, Vals),
    create_func_env(Params, Vals, env([[]], false, []), FuncEnv),
    reduce_stmt(config(Stmts, FuncEnv), config(_, FinalEnv)),
    has_declared(Name, FinalEnv, id(Name, _, R, _)),
    NewEnv = Env.
reduce(config(call(Name, Args), _), _) :-
    throw(undeclare_function(call(Name, Args))).

% Giảm danh sách đối số
reduce_args([], _, []).
reduce_args([E|Es], Env, [V|Vs]) :-
    reduce_all(config(E, Env), config(V, Env)),
    reduce_args(Es, Env, Vs).

% Tạo môi trường cho hàm
create_func_env([], [], Env, Env).
create_func_env([par(X, Type)|Ps], [V|Vs], env([L|L2], T, Procs), EnvOut) :-
    create_func_env(Ps, Vs, env([[id(X, var, V, Type)|L]|L2], T, Procs), EnvOut).

% Tìm hàm
lookup_func(Name, env(_, _, Procs), func(Name, Params, Type, Stmts)) :-
    member(func(Name, Params, Type, Stmts), Procs).

% Giảm biểu thức đầy đủ
reduce_all(config(V, Env), config(V, Env)) :- integer(V), !.
reduce_all(config(V, Env), config(V, Env)) :- float(V), !.
reduce_all(config(V, Env), config(V, Env)) :- is_bool(V), !.
reduce_all(config(V, Env), config(V, Env)) :- string(V), !.
reduce_all(config(E, Env), config(E2, Env)) :-
    reduce(config(E, Env), config(E1, Env)), !,
    reduce_all(config(E1, Env), config(E2, Env)).

% Giảm câu lệnh
reduce_stmt(config([], _), config([], _)).
reduce_stmt(config([Stmt|Stmts], Env), config([], NewEnv)) :-
    reduce_one_stmt(config(Stmt, Env), config(_, Env1)),
    reduce_stmt(config(Stmts, Env1), config([], NewEnv)).

reduce_one_stmt(config(assign(I, E), Env), config(_, NewEnv)) :-
    atom(I),
    reduce_all(config(E, Env), config(V, Env)),
    (   has_declared(I, Env, id(I, const, _, _)) ->
        throw(cannot_assign(assign(I, E)))
    ;   has_declared(I, Env, id(I, _, _, Type)) ->
        (   valid_type(V, Type) ->
            update_env(I, V, Env, NewEnv)
        ;   throw(type_mismatch(assign(I, E)))
        )
    ;   throw(undeclare_identifier(I))
    ).
reduce_one_stmt(config(block(Vars, Stmts), Env), config(_, NewEnv)) :-
    check_redeclarations(Vars),
    create_env(Vars, env([[]|Env], false, Env), LocalEnv),
    reduce_stmt(config(Stmts, LocalEnv), config(_, _)),
    NewEnv = Env.
reduce_one_stmt(config(if(E, S1), Env), config(_, NewEnv)) :-
    reduce_all(config(E, Env), config(V, Env)),
    (   is_bool(V) ->
        (   V = true -> reduce_one_stmt(config(S1, Env), config(_, NewEnv))
        ;   NewEnv = Env
        )
    ;   throw(type_mismatch(if(E, S1)))
    ).
reduce_one_stmt(config(if(E, S1, S2), Env), config(_, NewEnv)) :-
    reduce_all(config(E, Env), config(V, Env)),
    (   is_bool(V) ->
        (   V = true -> reduce_one_stmt(config(S1, Env), config(_, NewEnv))
        ;   reduce_one_stmt(config(S2, Env), config(_, NewEnv))
        )
    ;   throw(type_mismatch(if(E, S1, S2)))
    ).
reduce_one_stmt(config(while(E, S), Env), config(_, NewEnv)) :-
    reduce_all(config(E, Env), config(V, Env)),
    (   is_bool(V) ->
        set_loop_flag(Env, LoopEnv),
        (   V = true ->
            reduce_one_stmt(config(S, LoopEnv), config(Result, Env1)),
            (   Result = break -> NewEnv = Env1
            ;   Result = continue -> reduce_one_stmt(config(while(E, S), Env1), config(_, NewEnv))
            ;   reduce_one_stmt(config(while(E, S), Env1), config(_, NewEnv))
            )
        ;   NewEnv = Env
        )
    ;   throw(type_mismatch(while(E, S)))
    ).
reduce_one_stmt(config(do(Stmts, E), Env), config(_, NewEnv)) :-
    set_loop_flag(Env, LoopEnv),
    reduce_stmt(config(Stmts, LoopEnv), config(Result, Env1)),
    (   Result = break -> NewEnv = Env1
    ;   Result = continue ->
        reduce_all(config(E, Env1), config(V, Env1)),
        (   is_bool(V) ->
            (   V = true -> reduce_one_stmt(config(do(Stmts, E), Env1), config(_, NewEnv))
            ;   NewEnv = Env1
            )
        ;   throw(type_mismatch(do(Stmts, E)))
        )
    ;   reduce_all(config(E, Env1), config(V, Env1)),
        (   is_bool(V) ->
            (   V = true -> reduce_one_stmt(config(do(Stmts, E), Env1), config(_, NewEnv))
            ;   NewEnv = Env1
            )
        ;   throw(type_mismatch(do(Stmts, E)))
        )
    ).
reduce_one_stmt(config(loop(E, S), Env), config(_, NewEnv)) :-
    reduce_all(config(E, Env), config(N, Env)),
    (   integer(N), N >= 0 ->
        set_loop_flag(Env, LoopEnv),
        execute_loop(N, S, LoopEnv, NewEnv)
    ;   throw(type_mismatch(loop(E, S)))
    ).
reduce_one_stmt(config(break(null), Env), config(break, Env)) :-
    Env = env(_, true, _), !.
reduce_one_stmt(config(break(null), _), _) :-
    throw(break_not_in_loop(break(null))).
reduce_one_stmt(config(continue(null), Env), config(continue, Env)) :-
    Env = env(_, true, _), !.
reduce_one_stmt(config(continue(null), _), _) :-
    throw(continue_not_in_loop(continue(null))).
reduce_one_stmt(config(call(Name, Args), Env), config(_, NewEnv)) :-
    is_builtin(Name, proc),
    reduce_args(Args, Env, Vals),
    p_call_builtin(Name, Vals), !,
    NewEnv = Env.
reduce_one_stmt(config(call(Name, Args), Env), config(_, NewEnv)) :-
    lookup_proc(Name, Env, proc(Name, Params, Stmts)),
    length(Args, N), length(Params, N), !,
    reduce_args(Args, Env, Vals),
    create_func_env(Params, Vals, env([[]], false, []), ProcEnv),
    reduce_stmt(config(Stmts, ProcEnv), config(_, _)),
    NewEnv = Env.
reduce_one_stmt(config(call(Name, Args), _), _) :-
    throw(undeclare_procedure(call(Name, Args))).

% Thực thi vòng lặp
execute_loop(0, _, Env, Env) :- !.
execute_loop(N, S, Env, NewEnv) :-
    N > 0,
    reduce_one_stmt(config(S, Env), config(Result, Env1)),
    (   Result = break -> NewEnv = Env1
    ;   Result = continue ->
        N1 is N - 1,
        execute_loop(N1, S, Env1, NewEnv)
    ;   N1 is N - 1,
        execute_loop(N1, S, Env1, NewEnv)
    ).

% Tìm thủ tục
lookup_proc(Name, env(_, _, Procs), proc(Name, Params, Stmts)) :-
    member(proc(Name, Params, Stmts), Procs).

% Cập nhật môi trường
update_env(I, V, env([L|L2], T, Procs), env([L1|L2], T, Procs)) :-
    select(id(I, Type, _, Type2), L, id(I, Type, V, Type2), L1).
update_env(I, V, env([L|L2], T, Procs), env([L|L3], T, Procs)) :-
    update_env(I, V, env(L2, T, Procs), env(L3, T, Procs)).

% Đặt cờ vòng lặp
set_loop_flag(env(L, _, Procs), env(L, true, Procs)).

% Kiểm tra kiểu hợp lệ
valid_type(V, integer) :- integer(V).
valid_type(V, float) :- float(V).
valid_type(V, boolean) :- is_bool(V).
valid_type(V, string) :- string(V).
valid_type(_, unknown).