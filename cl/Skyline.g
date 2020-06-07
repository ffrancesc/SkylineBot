grammar Skyline;

root : skyline
     | assig ;


edifici : '(' num ',' num ',' num ')' ;

edificis : edifici  (',' edifici)*;

simple : edifici ;

compost : '[' edificis ']' ;

random : '{' num ',' num ',' num ',' num ',' num '}' ;

num : NUM ;

skyline : simple
        | compost
        | random
        | IDENT
        | '(' skyline ')'
        | '-' skyline
        | skyline '*' skyline
        | skyline '*' num
        | skyline '+' skyline
        | skyline '+' num
        | skyline '-' num ;

assig : IDENT ':=' skyline ;

NUM : [0-9]+ ;
IDENT : [a-zA-Z] [0-9a-zA-Z]*;


WS : [ \n]+ -> skip ;