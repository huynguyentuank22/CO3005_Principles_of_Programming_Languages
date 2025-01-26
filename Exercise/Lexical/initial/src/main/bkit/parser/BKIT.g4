grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;

// C1
ID: [a-z] [a-z0-9]+;

/* C2
REAL: INTPART DECPART | INTPART DECPART? EXPPART;
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]+;
fragment EXPPART: ('e' | 'E') '-'? [0-9]+;
*/

/* C3 
STRING: SingQ (~['] | SingQ SingQ)* SingQ;
fragment SingQ: '\'';
*/

/* C4 
IPv4: OCTEC '.' OCTEC '.' OCTEC '.' OCTEC;
fragment OCTEC: DIGIT
				| NON_ZERO_DIGIT DIGIT
				| '1' DIGIT DIGIT
				| '2' ([0-4] DIGIT | '5' [0-5]);
fragment DIGIT: [0-9]; 
fragment NON_ZERO_DIGIT: [1-9];
*/

/* C5
INTEGER: '0' | NON_ZERO_DIGIT DIGIT_UNDERSCORE* {self.text = self.text.replace('_', '')};
fragment DIGIT: [0-9];
fragment NON_ZERO_DIGIT: [1-9];
fragment DIGIT_UNDERSCORE: '_'? DIGIT+;	
*/

SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .  {raise ErrorToken(self.text)};
