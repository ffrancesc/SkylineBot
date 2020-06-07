grammar Skyline;

root : skyline
     | assig ;


edifici : '(' NUM ',' NUM ',' NUM ')' ;

edificis : edifici | edificis ',' edifici ;

simple : edifici ;

compost : '[' edificis ']' ;

random : '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}' ;

skyline : simple
        | compost
        | random
        | IDENT /*
        | '(' skyline ')'
        | '-' skyline
        | skyline '*' skyline
        | skyline '*' NUM
        | skyline '+' skyline
        | skyline '+' NUM
        | skyline '-' NUM */ ;

assig : IDENT ':=' skyline ;

NUM : [0-9]+ ;
IDENT : [a-zA-Z] [0-9a-zA-Z]*;


WS : [ \n]+ -> skip ;