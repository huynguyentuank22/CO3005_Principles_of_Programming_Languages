grammar MiniGo;

@lexer::header {
# Nguyen Tuan Huy - 2211253
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

program  : stmt+ EOF ;

decl: func_decl | var_decl | short_var_decl | const_decl | array_decl | short_array_decl | struct_decl | interface_decl;
assign: assign_array | assign_struct | access_struct;
call: func_call;

var_decl: VAR? IDENTIFIER (primitive_type (ASSIGN expr)? | ASSIGN expr) eos;
short_var_decl: IDENTIFIER DECLARE_ASSIGN expr eos;

const_decl: CONST IDENTIFIER ASSIGN expr eos;

func_decl: FUNC method? IDENTIFIER LB param_list? RB types? LCB stmt* RCB eos;
func_call: (IDENTIFIER DOT)? IDENTIFIER LB args? RB eos;
args: expr (COMMA expr)*;

method: LB IDENTIFIER IDENTIFIER RB;

param_list: param (COMMA param)*;
param: IDENTIFIER types?;  
types: primitive_type | array_type | IDENTIFIER;
literals: INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL | NIL_LITERAL;

// TYPE DECLARATION
primitive_type: INT | FLOAT | STRING | BOOLEAN;
// ARRAY TYPE
assign_array: IDENTIFIER index_ops+ ASSIGN expr eos;
array_decl: VAR IDENTIFIER (array_type | ASSIGN array_literal) eos;
short_array_decl: IDENTIFIER DECLARE_ASSIGN array_literal eos;
array_type: dimensions (primitive_type | IDENTIFIER);
dimensions: (LSB INT_LITERAL RSB)+;
// END ARRAY TYPE

// ARRAY LITERAL
array_literal: array_type ele_list;
ele_list: LCB ele (COMMA ele)* RCB;
ele: ele_list | literals;
// END ARRAY LITERAL

// STRUCT TYPE
access_struct: IDENTIFIER DOT IDENTIFIER ASSIGN expr eos;
assign_struct: IDENTIFIER DECLARE_ASSIGN struct_literal eos;
struct_decl: TYPE IDENTIFIER struct_type eos;
struct_type: STRUCT LCB fields* RCB;
fields: IDENTIFIER (primitive_type | array_type | struct_type | IDENTIFIER) eos;
// END STRUCT TYPE

// STRUCT LITERAL
struct_literal: IDENTIFIER LCB (field_lit (COMMA field_lit)*)? RCB;
field_lit: IDENTIFIER COLON expr;

// INTERFACE TYPE
interface_decl: TYPE IDENTIFIER interface_type eos;
interface_type: INTERFACE LCB method_decl* RCB;
method_decl: IDENTIFIER LB param_list? RB types? eos;
// END INTERFACE TYPE
// END TYPE DECLARATION

// EXPRESSION
expr: expr OR expr
    | expr AND expr
    | expr relational_ops expr
    | expr arithmetic_ops expr
    | NOT expr
    | SUB expr
    | expr index_ops+
    | expr DOT IDENTIFIER
    | primary_expr
    ;

primary_expr: IDENTIFIER
    | literals
    | LB expr RB
    ;
// END EXPRESSION

// STATEMENT
stmt: decl
    | assign
    | call
    | asm_stmt
    | if_stmt
    | for_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    ;

asm_stmt: IDENTIFIER index_ops* assign_ops expr eos;
if_stmt: IF LB expr RB LCB stmt* RCB else_if_stmt* (ELSE LCB stmt* RCB)? eos;
else_if_stmt: ELSE IF LB expr RB LCB stmt* RCB;
for_stmt: FOR for_clause LCB stmt* RCB eos;
for_clause: expr | fully_clause | range_clause;
fully_clause: init? eos expr? eos update?;
init: IDENTIFIER (ASSIGN | DECLARE_ASSIGN) expr;
update: IDENTIFIER index_ops* assign_ops expr;
range_clause: (IDENTIFIER | '_') COMMA IDENTIFIER DECLARE_ASSIGN RANGE IDENTIFIER;
break_stmt: BREAK eos;
continue_stmt: CONTINUE eos;
return_stmt: RETURN expr? eos;
// END STATEMENT

// OPERATORS
boolean_ops: NOT | AND | OR;
arithmetic_ops: ADD | SUB | MUL | DIV | MOD;
relational_ops: EQ | NEQ | GT | GE | LT | LE;
assign_ops: PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
index_ops: LSB expr RSB;
// END OPERATORS

// END OF STATEMENT
eos: SEMICOLON | EOS;

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

ASSIGN          : '=';
DECLARE_ASSIGN  : ':=';
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
COLON: ':';
SEMICOLON: ';';
// END SEPARATORS

// literals
INT_LITERAL: DECIMAL_LITERAL | BINARY_LITERAL | OCTAL_LITERAL | HEX_LITERAL;
DECIMAL_LITERAL: INT_PART;
BINARY_LITERAL: '0' [bB] [01]+;
OCTAL_LITERAL: '0' [oO] [0-7]+;
HEX_LITERAL: '0' [xX] [0-9a-fA-F]+;
fragment DIGIT: [0-9];
fragment NONZERO_DIGIT: [1-9];
fragment LETTER: [a-zA-Z];

FLOAT_LITERAL: INT_PART DEC_PART | INT_PART DEC_PART? EXP_PART;
fragment INT_PART: NONZERO_DIGIT DIGIT* | '0';
fragment DEC_PART: '.' DIGIT*;
fragment EXP_PART: [eE] [+-]? DIGIT+;

STRING_LITERAL: '"' CHAR* '"';
fragment CHAR: ESC | ~["\\\r\n];
fragment ESC: '\\' ( 'n' | 't' | 'r' | '"' | '\\' );
fragment INVALID_ESC: '\\' ~[ntr"\\];
BOOLEAN_LITERAL: TRUE | FALSE;

NIL_LITERAL: NIL;
// END literals

// IDENTIFIER
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT )*;
fragment UNDERSCORE: '_';
// END IDENTIFIER

// COMMENT
LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' (COMMENT | .)*? '*/' -> skip;
// END COMMENT

WS : [ \t\f\r]+ -> skip ; // skip spaces, tabs 
EOS: ([\r\n]+) {
    if self != ';':
        if self.check_EOS():
            self.text = ';'
            return self.SEMICOLON
        else:
            self.skip()
};

ERROR_CHAR: . {raise ErrorToken(self.text)};

ILLEGAL_ESCAPE: '"' CHAR* INVALID_ESC {
    illegal_string = str(self.text) 
    raise IllegalEscape(illegal_string[1:])
    };

UNCLOSE_STRING: '"' CHAR* ([\n\r] | EOF) {
    ESC = ['\r', '\n']
    text = str(self.text)
    if text[-1] in ESC:
        raise UncloseString(text[1:-1])
    else:
        raise UncloseString(text[1:])
    };

// mode NLSEMI;

// WS_NLSEMI: [ \t] -> skip;
// COMMENT_NLSEMI: '/*' ~[\r\n]*? '*/' -> skip;
// LINE_COMMENT_NLSEMI: '//' ~[\r\n]* -> skip;
// : ([\r\n]+ | ';' | '/*' .*? '*/' | EOF) -> mode(DEFAULT_MODE);
// OTHER: -> mode(DEFAULT_MODE), skip;