grammar MiniGo;

@lexer::header {
# Nguyen Tuan Huy - 2211253
# fix như tam, sua expression
# fix struct nested, for
from lexererr import *
}

@lexer::members {
def __init__(self, input):
    super().__init__(input)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.prev_token = None

def check_EOS(self):
    if not self.prev_token:
        return False
    tokens = [
        self.IDENTIFIER,
        self.INT_LITERAL, self.FLOAT_LITERAL, self.STRING_LITERAL, self.BOOLEAN_LITERAL, self.NIL_LITERAL,
        self.INT, self.FLOAT, self.STRING, self.BOOLEAN,
        self.RETURN, self.BREAK, self.CONTINUE,
        self.RB, self.RCB, self.RSB
    ]
    return self.prev_token.type in tokens

def emit(self):
    tk = self.type
    token = super().emit()
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    elif tk != '\n':
        self.prev_token = token
    return token
}

options{
	language=Python3;
}

program: decl+ EOF;

decl: var_decl | const_decl | array_decl | struct_decl | interface_decl | func_decl | method_decl; // short_var_decl short_array_decl 

var_decl: (decl_var_type_init | decl_var_init | decl_var_type) eos;
decl_var_type_init: VAR IDENTIFIER primitive_type DECLARE_ASSIGN expr;
decl_var_init: VAR IDENTIFIER DECLARE_ASSIGN expr;
decl_var_type: VAR IDENTIFIER (primitive_type | IDENTIFIER);

// CONST DECLARATION
const_decl: CONST IDENTIFIER DECLARE_ASSIGN expr eos;

// ARRAY DECLARATION
array_decl: (decl_arr | decl_arr_init) eos;

decl_arr: VAR IDENTIFIER array_type;
array_type: dimensions (primitive_type | IDENTIFIER);
dimensions: (LSB (INT_LITERAL | IDENTIFIER) RSB)+;

decl_arr_init: VAR IDENTIFIER DECLARE_ASSIGN array_literal;
array_literal: array_type ele_list;
ele_list: LCB (ele (COMMA ele)*)? RCB;
ele: ele_list | primitive_lit | IDENTIFIER | struct_literal;

// STRUCT DECLARATION
struct_decl: TYPE IDENTIFIER struct_type eos;
struct_type: STRUCT LCB fields+ RCB;
fields: IDENTIFIER (primitive_type | array_type | IDENTIFIER) eos; // struct_type

struct_literal: IDENTIFIER LCB struct_elements? RCB;
struct_elements: struct_ele (COMMA struct_ele)*;
struct_ele: IDENTIFIER ':' expr;

// INTERFACE DECLARATION
interface_decl: TYPE IDENTIFIER interface_type eos;
interface_type: INTERFACE LCB interface_field+ RCB;
interface_field: IDENTIFIER LB param_list? RB types? eos;


// FUNCTION DECLARATION
func_decl: FUNC IDENTIFIER LB param_list? RB types? block eos;
param_list: param (COMMA param)*;
param: id_list types;
id_list: IDENTIFIER (COMMA IDENTIFIER)*;
block: LCB stmt+ RCB;

// METHOD DECLARATION
method_decl: FUNC method IDENTIFIER LB param_list? RB types? block eos;
method: LB IDENTIFIER IDENTIFIER RB;


types: primitive_type | array_type | IDENTIFIER;
primitive_lit: INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL | NIL_LITERAL;
literals: primitive_lit | array_literal | struct_literal;
primitive_type: INT | FLOAT | STRING | BOOLEAN;

// FUNCTION CALL
func_call: IDENTIFIER LB expr_list? RB;

// EXPRESSION
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 relational_ops expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: (NOT | SUB) expr5 | primary_expr;

primary_expr: IDENTIFIER index_ops
            | primary_expr index_ops
            | primary_expr DOT IDENTIFIER
            | primary_expr DOT IDENTIFIER LB expr_list? RB
            | operand
            ;
expr_list: expr (COMMA expr_list)*;
    
operand:  literals
        | IDENTIFIER
        | func_call
        | LB expr RB
        ;
// END EXPRESSION

// STATEMENT
stmt: decl_stmt
    | asm_stmt
    | if_stmt
    | for_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;

decl_stmt: var_decl | const_decl | array_decl;

// asm_stmt: IDENTIFIER index_ops* assign_ops expr eos;
asm_stmt: asm eos;
asm: lhs assign_ops rhs;
lhs: IDENTIFIER | array_elem | struct_elem;
array_elem: IDENTIFIER index_ops+;
struct_elem: (IDENTIFIER | array_elem) struct_ops+;
struct_ops: DOT (IDENTIFIER | array_elem | func_call); // khac
rhs: expr;

if_stmt: IF LB expr RB block else_if_stmt* (ELSE block)? eos;
else_if_stmt: ELSE IF LB expr RB block;

for_stmt: FOR for_clause block eos;
for_clause: expr | fully_clause | range_clause;

fully_clause: init eos expr eos update;
init: asm | decl_var_init;
update: asm;

range_clause: (IDENTIFIER | '_') COMMA IDENTIFIER ASSIGN RANGE IDENTIFIER;

break_stmt: BREAK eos;
continue_stmt: CONTINUE eos;
call_stmt: (func_call | struct_elem | array_elem) eos;
return_stmt: RETURN expr? eos;
// END STATEMENT

// OPERATORS
boolean_ops: NOT | AND | OR;
arithmetic_ops: ADD | SUB | MUL | DIV | MOD;
relational_ops: EQ | NEQ | GT | GE | LT | LE;
assign_ops: ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
index_ops: LSB expr RSB;
// END OPERATORS

// END OF STATEMENT
eos: SEMICOLON | EOS;

BOOLEAN_LITERAL: TRUE | FALSE;
NIL_LITERAL: NIL;
// KEYWORDS
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';
// END KEYWORDS

// OPERATORS
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQ  : '==';
NEQ : '!=';
LT  : '<';
LE  : '<=';
GT  : '>';
GE  : '>=';

AND : '&&';
OR  : '||';
NOT : '!';

DECLARE_ASSIGN  : '=';
ASSIGN          : ':=';
PLUS_ASSIGN     : '+=' ;
MINUS_ASSIGN    : '-=' ;
MULT_ASSIGN     : '*=' ;
DIV_ASSIGN      : '/=' ;
MOD_ASSIGN      : '%=' ;

DOT: '.';
// END OPERATORS

// SEPARATORS
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
COMMA: ',';
// COLON: ':';
SEMICOLON: ';';
// END SEPARATORS

// literals
INT_LITERAL: DECIMAL_LITERAL | BINARY_LITERAL | OCTAL_LITERAL | HEX_LITERAL;
DECIMAL_LITERAL: NONZERO_DIGIT DIGIT* | '0';
BINARY_LITERAL: '0' [bB] [01]+;
OCTAL_LITERAL: '0' [oO] [0-7]+;
HEX_LITERAL: '0' [xX] [0-9a-fA-F]+;
fragment DIGIT: [0-9];
fragment NONZERO_DIGIT: [1-9];
fragment LETTER: [a-zA-Z];

FLOAT_LITERAL: INT_PART DEC_PART | INT_PART DEC_PART EXP_PART;
fragment INT_PART: DIGIT+;
fragment DEC_PART: '.' DIGIT*;
fragment EXP_PART: [eE] [+-]? DIGIT+;

STRING_LITERAL: '"' CHAR* '"';
fragment CHAR: ESC | ~["\\\r\n];
fragment ESC: '\\' ( 'n' | 't' | 'r' | '"' | '\\' );
fragment INVALID_ESC: '\\' ~[ntr"\\];

// END literals

// IDENTIFIER
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;
fragment UNDERSCORE: '_';
// END IDENTIFIER

// COMMENT
LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' (COMMENT | .)*? '*/' -> skip;
// END COMMENT

WS : [ \t\f\r]+ -> skip ; // skip spaces, tabs 
EOS: ([\r\n]+) {
    if self.check_EOS():
        self.text = ';'
    else:
        self.skip()
};

ERROR_CHAR: . {raise ErrorToken(self.text)};

ILLEGAL_ESCAPE: '"' CHAR* INVALID_ESC { raise IllegalEscape(self.text) };

UNCLOSE_STRING: '"' CHAR* ([\r\n]+ | EOF) {
    ESC = ['\r', '\n']
    text = str(self.text)
    while text[-1] in ESC:
        text = text[:-1]
    raise UncloseString(text[:])
};