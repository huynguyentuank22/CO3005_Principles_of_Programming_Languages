grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/* C1
program: (vardecl | funcdecl)+ EOF; // write for program rule here using vardecl and funcdecl

vardecl: 'vardecl' ;

funcdecl: 'funcdecl' ;
*/

/* C2 
program: (var_decl | func_decl)+ EOF;// write your rule here

//And some other rules for variable declaration, function declaration and other rules
var_decl: types var SEMICOLON;
var: ID (COMMA ID)*;

func_decl: types ID LB params? RB body;
params: param (SEMICOLON param)*;
param: types ID (COMMA ID)*; 
body: 'body';
types: (INT | FLOAT);

INT: 'int';
FLOAT: 'float';
SEMICOLON: ';';
COMMA: ',';
LB: '(';
RB: ')';
*/

/* C3 
program: (var_decl | func_decl)+ EOF;// write your rule here

//And some other rules for variable declaration, function declaration and other rules
var_decl: types var SEMICOLON;
var: ID (COMMA ID)*;

func_decl: types ID LB params? RB body;
params: param (SEMICOLON param)*;
param: types ID (COMMA ID)*; 
body: LCB stm* RCB;
stm: var_decl | assign_stm | call_stm | return_stm;
assign_stm: ID ASSIGN expr SEMICOLON;
call_stm: ID LB (expr (COMMA expr)*) RB SEMICOLON;
return_stm: RETURN expr SEMICOLON;
expr: 'expr';
types: (INT | FLOAT);

INT: 'int';
FLOAT: 'float';
RETURN: 'return';
SEMICOLON: ';';
COMMA: ',';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
ASSIGN: '=';
*/

/* C4 */
program: (var_decl | func_decl)+ EOF;// write your rule here

//And some other rules for variable declaration, function declaration and other rules
var_decl: types var SEMICOLON;
var: ID (COMMA ID)*;

func_decl: types ID LB params? RB body;
params: param (SEMICOLON param)*;
param: types ID (COMMA ID)*; 
body: LCB stm* RCB;
stm: var_decl | assign_stm | call_stm | return_stm;
assign_stm: ID ASSIGN expr SEMICOLON;
call_stm: ID LB (expr (COMMA expr)*) RB SEMICOLON;
return_stm: RETURN expr SEMICOLON;
expr: expr ('*' | '/') expr
	| expr '-' expr
	| expr '+' expr
	| operand; 
operand: func | ID | INTLIT | FLOATLIT | LB expr RB;
func: ID LB (expr (COMMA expr)*) RB;
types: (INT | FLOAT);

INT: 'int';
FLOAT: 'float';
RETURN: 'return';
SEMICOLON: ';';
COMMA: ',';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
ASSIGN: '='; 

ID: [a-zA-Z]+ ;
INTLIT: [0-9]+;
FLOATLIT: INTLIT '.' INTLIT;

WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
