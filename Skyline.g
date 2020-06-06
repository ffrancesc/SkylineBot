grammar Skyline;

root : skyline EOF ;

literal : '(' NUM ',' NUM ',' NUM ')' ;

skyline : literal
        | '(' skyline ')'
        | '-' skyline
        | skyline '*' skyline
        | skyline '*' NUM
        | skyline '+' skyline
        | skyline '+' NUM
        | skyline '-' NUM
        ;

assig : IDENT ':=' skyline ;

DIGIT : [0-9] ;
LLETRA : [a-z] | [A-Z] ;

NUM : DIGIT+ ;
IDENT : LLETRA (LLETRA | DIGIT)*;


WS : [ \n]+ -> skip ;