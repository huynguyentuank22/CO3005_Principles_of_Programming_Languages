% main program

% Kiểm tra giá trị boolean
boolean(true).
boolean(false).

% Chương trình chính
reduce_prog([Var, Procs, Body]) :-
    check_redeclarations(Var),
    create_env(Var, env([[]], false, Procs), Env0),
    check_procs_phase1(Procs, Env0, Env),
    check_proc_bodies(Procs, Env, UpdatedEnv), % Nhận UpdatedEnv
    reduce_stmt(config(Body, UpdatedEnv), config([], _), UpdatedEnv).

check_proc_bodies([], Env, Env).
check_proc_bodies([func(Name, Params, Type, Stmts)|Rest], GlobalEnv, FinalEnv) :-
    check_params(Params),
    length(Params, N),
    length(DummyArgs, N),
    create_func_env(Params, DummyArgs, env([[id(Name, var, undef, Type)]], false, []), FuncEnv),
    reduce_stmt(config(Stmts, FuncEnv), config([], _), GlobalEnv),
    check_proc_bodies(Rest, GlobalEnv, FinalEnv).
check_proc_bodies([proc(Name, Params, Stmts)|Rest], GlobalEnv, FinalEnv) :-
    check_params(Params),
    % Tạo FuncEnv với danh sách đối số giả (không dùng giá trị thực)
    length(Params, N),
    length(DummyArgs, N),
    create_func_env(Params, DummyArgs, env([[]], false, []), FuncEnv),
    reduce_stmt(config(Stmts, FuncEnv), config([], _), GlobalEnv),
    check_proc_bodies(Rest, GlobalEnv, FinalEnv).

% Kiểm tra khai báo lại cho biến và hằng
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

% Thêm một định danh vào môi trường
add_to_env(Id, env([Scope|Rest], LoopFlag, Procs), env([NewScope|Rest], LoopFlag, Procs)) :-
    NewScope = [Id|Scope].

% Kiểm tra danh sách tham số (không thêm vào Env)
check_params(Params) :-
    check_params(Params, []).

check_params([], _).
check_params([par(Name, Type)|Rest], Seen) :-
    (   member(Name, Seen) ->
        throw(redeclare_identifier(par(Name, Type)))
    ;   check_params(Rest, [Name|Seen])
    ).

% Giai đoạn 1: Kiểm tra khai báo func/proc và chỉ thêm tên vào Env
check_procs_phase1(Procs, EnvIn, EnvOut) :-
    check_procs_phase1(Procs, EnvIn, EnvOut, []).

check_procs_phase1([], Env, Env, _).
check_procs_phase1([func(Name, Params, Type, _)|Rest], EnvIn, EnvOut, Seen) :-
    check_params(Params),  % Kiểm tra trùng lặp tham số
    (   is_builtin(Name, _) ->
        throw(redeclare_function(Name))
    ;   has_declared(Name, EnvIn, _) ->
        throw(redeclare_function(Name))
    ;   member(Name-_, Seen) ->
        throw(redeclare_function(Name))
    ;   add_to_env(id(Name, func, undef, Type), EnvIn, EnvTemp),
        check_procs_phase1(Rest, EnvTemp, EnvOut, [Name-func|Seen])
    ).
check_procs_phase1([proc(Name, Params, _)|Rest], EnvIn, EnvOut, Seen) :-
    check_params(Params),  % Kiểm tra trùng lặp tham số
    (   is_builtin(Name, _) ->
        throw(redeclare_procedure(Name))
    ;   has_declared(Name, EnvIn, _) ->
        throw(redeclare_procedure(Name))
    ;   member(Name-_, Seen) ->
        throw(redeclare_procedure(Name))
    ;   add_to_env(id(Name, proc, undef, unknown), EnvIn, EnvTemp),
        check_procs_phase1(Rest, EnvTemp, EnvOut, [Name-proc|Seen])
    ).

% Kiểm tra khai báo định danh
has_declared(X, env([L|_], _, _), id(X, Kind, Val, Type)) :- 
    member(id(X, Kind, Val, Type), L), !.
has_declared(X, env([_|Rest], LoopFlag, Procs), R) :- 
    Rest \= [], % Ngăn đệ quy vô hạn
    has_declared(X, env(Rest, LoopFlag, Procs), R).

% Kiểm tra khai báo trong cả môi trường cục bộ và toàn cục
has_declared_with_global(X, LocalEnv, GlobalEnv, Id) :-
    (   has_declared(X, LocalEnv, Id) -> true
    ;   has_declared(X, GlobalEnv, Id)
    ).

% Tạo môi trường (chỉ thêm biến và hằng)
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
    (   boolean(V1) ->
        R is \V1
    ;   throw(type_mismatch(bnot(E1)))
    ).
reduce(config(band(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    (   V1 = false ->
        R = false
    ;   reduce_all(config(E2, Env), config(V2, Env)),
        (   boolean(V2) ->
            (V2 = false -> R = false ; R = true)
        ;   throw(type_mismatch(band(E1, E2)))
        )
    ).
reduce(config(bor(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    (   V1 = true ->
        R = true
    ;   reduce_all(config(E2, Env), config(V2, Env)),
        (   boolean(V2) ->
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
    (   (integer(V1), integer(V2); boolean(V1), boolean(V2)) ->
        R = (V1 =:= V2)
    ;   throw(type_mismatch(eq(E1, E2)))
    ).
reduce(config(ne(E1, E2), Env), config(R, Env)) :-
    reduce_all(config(E1, Env), config(V1, Env)),
    reduce_all(config(E2, Env), config(V2, Env)),
    (   (integer(V1), integer(V2); boolean(V1), boolean(V2)) ->
        R = (V1 =\= V2)
    ;   throw(type_mismatch(ne(E1, E2)))
    ).
reduce(config(I, Env), config(V, Env)) :-
    atom(I),
    (   has_declared(I, Env, id(I, _, V, _)) ->
        (   V = undef -> throw(invalid_expression(I)) ; true )
    ;   throw(undeclare_identifier(I))
    ).
% Giảm biểu thức cho lời gọi hàm
reduce(config(call(Name, Args), Env), config(R, NewEnv)) :-
    is_builtin(Name, func),
    valid_builtin_args(Name, Args, Env, func, R),
    NewEnv = Env.
reduce(config(call(Name, Args), Env), config(R, NewEnv)) :-
    lookup_func(Name, Env, func(Name, Params, Type, Stmts)),
    length(Args, NArgs), length(Params, NParams),
    (   NArgs = NParams ->
        reduce_args(Args, Env, Vals),
        create_func_env(Params, Vals, env([[id(Name, var, undef, Type)]], false, Env), FuncEnv),
        reduce_stmt(config(Stmts, FuncEnv), config([], FinalEnv), Env),
        has_declared(Name, FinalEnv, id(Name, _, R, _)),
        (   R \= undef ->
            (   valid_type(R, Type) -> true
            ;   throw(type_mismatch(call(Name, Args)))
            )
        ;   throw(invalid_expression(call(Name, Args)))
        ),
        NewEnv = Env
    ;   throw(wrong_number_of_argument(call(Name, Args)))
    ).
reduce(config(call(Name, Args), _), _) :-
    throw(undeclare_function(call(Name, Args))).

% Giảm danh sách đối số
reduce_args([], _, []).
reduce_args([E|Es], Env, [V|Vs]) :-
    reduce_all(config(E, Env), config(V, Env)),
    reduce_args(Es, Env, Vs).

% Tạo môi trường cho hàm (thêm params khi thực thi)
create_func_env([], [], Env, Env).
create_func_env([par(X, Type)|Ps], [V|Vs], env([L|L2], T, Procs), EnvOut) :-
    create_func_env(Ps, Vs, env([[id(X, var, V, Type)|L]|L2], T, Procs), EnvOut).

% Tìm hàm
lookup_func(Name, env(_, _, Procs), func(Name, Params, Type, Stmts)) :-
    member(func(Name, Params, Type, Stmts), Procs).
% Kiểm tra kiểu hợp lệ cho đối số của hàm built-in
valid_builtin_args(Name, Args, Env, func, R) :-
    length(Args, 1),
    [Arg] = Args,
    reduce_all(config(Arg, Env), config(V, _)),
    (   valid_builtin_type(Name, V) ->
        reduce_args(Args, Env, Vals),
        p_call_builtin(Name, Vals, R)
    ;   throw(type_mismatch(call(Name, Args)))
    ).
valid_builtin_args(Name, Args, Env, proc, _) :-
    length(Args, 1),
    [Arg] = Args,
    reduce_all(config(Arg, Env), config(V, _)),
    (   valid_builtin_type(Name, V) ->
        reduce_args(Args, Env, Vals),
        p_call_builtin(Name, Vals)
    ;   throw(type_mismatch(call(Name, Args)))
    ).

valid_builtin_type(writeBool, V) :- boolean(V), !.
valid_builtin_type(writeInt, V) :- integer(V), !.
valid_builtin_type(writeReal, V) :- float(V), !.
valid_builtin_type(writeStr, V) :- string(V), !.
valid_builtin_type(writeBoolLn, V) :- boolean(V), !.
valid_builtin_type(writeIntLn, V) :- integer(V), !.
valid_builtin_type(writeRealLn, V) :- float(V), !.
valid_builtin_type(writeStrLn, V) :- string(V), !.
valid_builtin_type(Name, _) :- member(Name, [readInt, readReal, readBool, writeLn]), !.
% Giảm biểu thức đầy đủ
reduce_all(config(V, Env), config(V, Env)) :- integer(V), !.
reduce_all(config(V, Env), config(V, Env)) :- float(V), !.
reduce_all(config(V, Env), config(V, Env)) :- boolean(V), !.
reduce_all(config(V, Env), config(V, Env)) :- string(V), !.
reduce_all(config(E, Env), config(V, Env)) :-
    atom(E),
    (   has_declared(E, Env, id(E, _, V, _)) ->
        (   V = undef -> throw(invalid_expression(E)) ; true )
    ;   throw(undeclare_identifier(E))
    ), !.
reduce_all(config(E, Env), config(E2, Env)) :-
    reduce(config(E, Env), config(E1, Env)),
    reduce_all(config(E1, Env), config(E2, Env)).

% Giảm câu lệnh
reduce_stmt(config([], Env), config([], Env), _).
reduce_stmt(config([Stmt|Stmts], Env), config([], NewEnv), GlobalEnv) :-
    (   is_list(Stmt) ->
        reduce_one_stmt(config(block(Stmt, []), Env), config(_, Env1), GlobalEnv)
    ;   reduce_one_stmt(config(Stmt, Env), config(_, Env1), GlobalEnv)
    ),
    reduce_stmt(config(Stmts, Env1), config([], NewEnv), GlobalEnv).

% Định nghĩa predicate helper: kiểm tra redeclaration trong local scope
is_local_declared(X, env([Scope|_], _, _)) :-
    member(id(X, _, _, _), Scope).

% Xử lý khai báo biến ở mức lệnh (cho proc, func, ...)
reduce_one_stmt(config(var(X, Type), Env), config(_, NewEnv), _) :-
    (   is_local_declared(X, Env) -> throw(redeclare_identifier(var(X, Type))) ; true ),
    add_to_env(id(X, var, undef, Type), Env, NewEnv).

reduce_one_stmt(config(const(X, Val), Env), config(_, NewEnv), _) :-
    (   is_local_declared(X, Env) -> throw(redeclare_identifier(const(X, Val))) ; true ),
    add_to_env(id(X, const, Val, unknown), Env, NewEnv).

reduce_one_stmt(config(assign(I, E), Env), config(_, NewEnv), GlobalEnv) :-
    atom(I),
    reduce_all(config(E, Env), config(V, Env)),
    (   has_declared_with_global(I, Env, GlobalEnv, id(I, Kind, _, Type)) ->
        (   Kind = const -> throw(cannot_assign(assign(I, E)))
        ;   valid_type(V, Type) ->
            (   has_declared(I, Env, _) -> update_env(I, V, Env, NewEnv)
            ;   update_env(I, V, GlobalEnv, NewEnv) % Cập nhật trực tiếp vào GlobalEnv
            )
        ;   throw(type_mismatch(assign(I, E)))
        )
    ;   throw(undeclare_identifier(I))
    ).

reduce_one_stmt(config(block(Vars, Stmts), Env), config(_, NewEnv), GlobalEnv) :-
    check_redeclarations(Vars),
    create_env(Vars, env([[]|Env], false, Env), LocalEnv),
    reduce_stmt(config(Stmts, LocalEnv), config([], _), GlobalEnv),
    NewEnv = Env.

reduce_one_stmt(config(if(E, S1), Env), config(_, NewEnv), GlobalEnv) :-
    reduce_all(config(E, Env), config(V, Env)),
    (   boolean(V) ->
        (   V = true -> reduce_one_stmt(config(S1, Env), config(_, NewEnv), GlobalEnv)
        ;   NewEnv = Env
        )
    ;   throw(type_mismatch(if(E, S1)))
    ).

reduce_one_stmt(config(if(E, S1, S2), Env), config(_, NewEnv), GlobalEnv) :-
    reduce_all(config(E, Env), config(V, Env)),
    (   boolean(V) ->
        (   V = true -> reduce_one_stmt(config(S1, Env), config(_, NewEnv), GlobalEnv)
        ;   reduce_one_stmt(config(S2, Env), config(_, NewEnv), GlobalEnv)
        )
    ;   throw(type_mismatch(if(E, S1, S2)))
    ).

reduce_one_stmt(config(while(E, S), Env), config(_, NewEnv), GlobalEnv) :-
    reduce_all(config(E, Env), config(V, Env)),
    (   boolean(V) ->
        set_loop_flag(Env, LoopEnv),
        (   V = true ->
            reduce_one_stmt(config(S, LoopEnv), config(Result, Env1), GlobalEnv),
            (   Result = break -> NewEnv = Env1
            ;   Result = continue -> reduce_one_stmt(config(while(E, S), Env1), config(_, NewEnv), GlobalEnv)
            ;   reduce_one_stmt(config(while(E, S), Env1), config(_, NewEnv), GlobalEnv)
            )
        ;   NewEnv = Env
        )
    ;   throw(type_mismatch(while(E, S)))
    ).

reduce_one_stmt(config(do(Stmts, E), Env), config(_, NewEnv), GlobalEnv) :-
    set_loop_flag(Env, LoopEnv),
    reduce_stmt(config(Stmts, LoopEnv), config(Result, Env1), GlobalEnv),
    (   Result = break ->
        NewEnv = Env1
    ;   % Gộp nhánh continue và mặc định
        reduce_all(config(E, Env1), config(V, Env1)),
        (   boolean(V) ->
            (   V = true ->
                reduce_one_stmt(config(do(Stmts, E), Env1), config(_, NewEnv), GlobalEnv)
            ;   NewEnv = Env1
            )
        ;   throw(type_mismatch(do(Stmts, E)))
        )
    ).

reduce_one_stmt(config(loop(E, S), Env), config(_, NewEnv), GlobalEnv) :-
    reduce_all(config(E, Env), config(N, Env)),
    (   integer(N), N >= 0 ->
        set_loop_flag(Env, LoopEnv),
        execute_loop(N, S, LoopEnv, NewEnv, GlobalEnv)
    ;   throw(type_mismatch(loop(E, S)))
    ).

reduce_one_stmt(config(break(null), Env), config(break, Env), _) :-
    Env = env(_, true, _), !.
reduce_one_stmt(config(break(null), _), _, _) :-
    throw(break_not_in_loop(break(null))).
reduce_one_stmt(config(continue(null), Env), config(continue, Env), _) :-
    Env = env(_, true, _), !.
reduce_one_stmt(config(continue(null), _), _, _) :-
    throw(continue_not_in_loop(continue(null))).

reduce_one_stmt(config(call(Name, Args), Env), config(_, NewEnv), GlobalEnv) :-
    is_builtin(Name, func),
    length(Args, 1),
    (   valid_builtin_args(Name, Args, Env, func, _) ->
        NewEnv = Env
    ;   throw(type_mismatch(call(Name, Args)))
    ), !.
reduce_one_stmt(config(call(Name, Args), Env), config(_, NewEnv), GlobalEnv) :-
    is_builtin(Name, proc),
    length(Args, 1),
    (   valid_builtin_args(Name, Args, Env, proc, _) ->
        NewEnv = Env
    ;   throw(type_mismatch(call(Name, Args)))
    ), !.
reduce_one_stmt(config(call(Name, Args), Env), config(_, NewEnv), GlobalEnv) :-
    lookup_func(Name, Env, func(Name, Params, Type, Stmts)),
    length(Args, NArgs), length(Params, NParams),
    (   NArgs = NParams ->
        reduce_args(Args, Env, Vals),
        create_func_env(Params, Vals, env([[id(Name, var, undef, Type)]], false, GlobalEnv), FuncEnv),
        reduce_stmt(config(Stmts, FuncEnv), config([], FinalEnv), GlobalEnv),
        has_declared(Name, FinalEnv, id(Name, _, R, _)),
        (   R \= undef ->
            (   valid_type(R, Type) -> true
            ;   throw(type_mismatch(call(Name, Args)))
            )
        ;   throw(invalid_expression(call(Name, Args)))
        ),
        NewEnv = Env
    ;   throw(wrong_number_of_argument(call(Name, Args)))
    ).
reduce_one_stmt(config(call(Name, Args), Env), config(_, NewEnv), GlobalEnv) :-
    lookup_proc(Name, Env, proc(Name, Params, Stmts)),
    length(Args, NArgs), length(Params, NParams),
    (   NArgs = NParams ->
        reduce_args(Args, Env, Vals),
        create_func_env(Params, Vals, env([[]], false, GlobalEnv), ProcEnv),
        reduce_stmt(config(Stmts, ProcEnv), config([], _), GlobalEnv),
        NewEnv = Env
    ;   throw(wrong_number_of_argument(call(Name, Args)))
    ).
reduce_one_stmt(config(call(Name, Args), _), config(_, _), _) :-
    throw(undeclare_procedure(call(Name, Args))).

% Thực thi vòng lặp
execute_loop(0, _, Env, Env, _) :- !.
execute_loop(N, S, Env, NewEnv, GlobalEnv) :-
    N > 0,
    reduce_one_stmt(config(S, Env), config(Result, Env1), GlobalEnv),
    (   Result = break -> NewEnv = Env1
    ;   Result = continue ->
        N1 is N - 1,
        execute_loop(N1, S, Env1, NewEnv, GlobalEnv)
    ;   N1 is N - 1,
        execute_loop(N1, S, Env1, NewEnv, GlobalEnv)
    ).

% Tìm thủ tục
lookup_proc(Name, env(_, _, Procs), proc(Name, Params, Stmts)) :-
    member(proc(Name, Params, Stmts), Procs).

% Cập nhật môi trường
update_env(I, V, env([L|L2], T, Procs), env([L1|L2], T, Procs)) :-
    select(id(I, Type, _, Type2), L, id(I, Type, V, Type2), L1), !.
update_env(I, V, env([L|L2], T, Procs), env([L|L3], T, Procs)) :-
    L2 \= [], % Ngăn đệ quy vô hạn
    update_env(I, V, env(L2, T, Procs), env(L3, T, Procs)).

% Đặt cờ vòng lặp
set_loop_flag(env(L, _, Procs), env(L, true, Procs)).

% Kiểm tra kiểu hợp lệ
valid_type(V, integer) :- integer(V).
valid_type(V, float) :- float(V).
valid_type(V, boolean) :- boolean(V).
valid_type(V, string) :- string(V).
valid_type(_, unknown).