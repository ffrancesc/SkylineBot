grammar Skyline;

root : skyline EOF
     | assig EOF ;

literal : '(' NUM ',' NUM ',' NUM ')';

skyline : literal
        | '(' skyline ')'
        | '-' skyline
        | skyline '*' skyline
        | skyline '*' NUM
        | skyline '+' skyline
        | skyline '+' NUM
        | skyline '-' NUM ;

assig : IDENT ':=' skyline ;

NUM : [0-9]+ ;
IDENT : [a-zA-Z] [0-9a-zA-Z]*;


WS : [ \n]+ -> skip ;