;MOV C, 5;

;MOV D, C;

;MOV D, [5];

;MOV A, 6;

;MOV D, [A]


;MOV [0xff], 5;

;MOV C, 0xf8;
;MOV [0xff], C;

;MOV [0xfe], 18;

;MOV [0xff], [0x2e];

;MOV [0xf8], 0xfe

;MOV C, 0xf8;

;MOV D, 0x33;

;MOV [C], D;


;MOV [0xf0], 0xee;


;MOV D, 0x30

;MOV C, 0x18;

;MOV [C], [0x30];

MOV D, 1
ADD D, 5

hlt;
