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

;MOV D, 0
;MOV C, 0
;ADD D, C
;MOV D, 5
;INC D
;INC D
;DEC D

;MOV C, 7

;MOV D, 2

;CMP C, D
;AND D, C
;OR D, C
;XOR D, C
;MOV D, 0xF0
;NOT D

  ;MOV D, 1
  ;JMP decrease


;increase:
;  INC D
;  CMP D, 5
;  JO increase
;decrease:
;  DEC D
;  CMP D, 0
;  JZ increase
;  JMP decrease

  MOV SS, 1
  MOV SP, 0x10
  MOV D, 10
  
  PUSH D
  PUSH 1
  
  POP C
  POP B
  MOV A, C

  ADD A, B
  MOV D, A

  HLT
