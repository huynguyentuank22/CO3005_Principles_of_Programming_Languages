grammar MiniGo;

@lexer::header {
# Nguyen Tuan Huy - 2211253
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : stmt+ EOF ;

decl: func_decl | var_decl | const_decl | array_decl | struct_decl | interface_decl;
assign: assign_array | assign_struct | access_struct;
call: func_call;

var_decl: VAR? IDENTIFIER (primitive_type (ASSIGN expr)? | ASSIGN expr) SEMICOLON?;

const_decl: CONST IDENTIFIER ASSIGN expr SEMICOLON;

func_decl: FUNC method? IDENTIFIER LB param_list? RB types? LCB stmt* RCB SEMICOLON?;
func_call: (IDENTIFIER DOT)? IDENTIFIER LB args? RB SEMICOLON?;
args: expr (COMMA expr)*;

method: LB IDENTIFIER IDENTIFIER RB;

param_list: param (COMMA param)*;
param: IDENTIFIER types?;  
types: primitive_type | array_type | IDENTIFIER;
literals: INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL | NIL_LITERAL;

// TYPE DECLARATION
primitive_type: INT | FLOAT | STRING | BOOLEAN;
// ARRAY TYPE
assign_array: IDENTIFIER index_ops+ ASSIGN expr SEMICOLON?;
array_decl: VAR? IDENTIFIER (array_type | ASSIGN array_literal) SEMICOLON?;
array_type: dimensions (primitive_type | IDENTIFIER);
dimensions: (LSB INT_LITERAL RSB)+;
// END ARRAY TYPE

// ARRAY LITERAL
array_literal: array_type ele_list;
ele_list: LCB ele (COMMA ele)* RCB;
ele: ele_list | literals;
// END ARRAY LITERAL

// STRUCT TYPE
access_struct: IDENTIFIER DOT IDENTIFIER ASSIGN expr SEMICOLON?;
assign_struct: IDENTIFIER ASSIGN struct_literal SEMICOLON?;
struct_decl: TYPE IDENTIFIER struct_type;
struct_type: STRUCT LCB fields* RCB;
fields: IDENTIFIER (primitive_type | array_type | struct_type | IDENTIFIER) SEMICOLON?;
// END STRUCT TYPE

// STRUCT LITERAL
struct_literal: IDENTIFIER LCB (field_lit (COMMA field_lit)*)? RCB;
field_lit: IDENTIFIER COLON expr;

// INTERFACE TYPE
interface_decl: TYPE IDENTIFIER interface_type;
interface_type: INTERFACE LCB method_decl* RCB;
method_decl: IDENTIFIER LB param_list? RB types? SEMICOLON?;
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

asm_stmt: IDENTIFIER index_ops* assign_ops expr SEMICOLON?;
if_stmt: IF LB expr RB LCB stmt* RCB else_if_stmt* (ELSE LCB stmt* RCB)?;
else_if_stmt: ELSE IF LB expr RB LCB stmt* RCB;
for_stmt: FOR for_clause LCB stmt* RCB;
for_clause: expr | fully_clause | range_clause;
fully_clause: var_decl? SEMICOLON expr SEMICOLON asm_stmt?;
range_clause: (IDENTIFIER | '_') COMMA IDENTIFIER ASSIGN RANGE IDENTIFIER;
break_stmt: BREAK SEMICOLON;
continue_stmt: CONTINUE SEMICOLON;
return_stmt: RETURN expr? SEMICOLON;
// END STATEMENT

// OPERATORS
boolean_ops: NOT | AND | OR;
arithmetic_ops: ADD | SUB | MUL | DIV | MOD;
relational_ops: EQ | NEQ | GT | GE | LT | LE;
assign_ops: PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
index_ops: LSB expr RSB;
// END OPERATORS

// COMMENT
LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' (COMMENT | .)*? '*/' -> skip;
// END COMMENT

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

EQ: '==';
NEQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

ASSIGN      : ':'? '=' ;
PLUS_ASSIGN : '+=' ;
MINUS_ASSIGN: '-=' ;
MULT_ASSIGN : '*=' ;
DIV_ASSIGN  : '/=' ;
MOD_ASSIGN  : '%=' ;

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


NL: '\n' -> skip; //skip newlines

WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs 

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