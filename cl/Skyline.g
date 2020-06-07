grammar Skyline;

root : skyline
     | assig ;

edifici : '(' num ',' num ',' num ')' ;

edificis : edifici  (',' edifici)*;

simple : edifici ;

compost : '[' edificis ']' ;

random : '{' num ',' num ',' num ',' num ',' num '}' ;

skyline : simple
        | compost
        | random
        | ident
        | '(' skyline ')'
        | '-' skyline
        | skyline '*' skyline
        | skyline '*' num
        | skyline '+' skyline
        | skyline '+' num
        | skyline '-' num ;

assig : ident ':=' skyline ;

num : NUM ;

ident : IDENT;

NUM : [0-9]+ ;
IDENT : [a-zA-Z] [0-9a-zA-Z]*;


WS : [ \n]+ -> skip ;