LDX #0
LOOP:
LDA $FE
STA $200,X
INX
CPX #0
BEQ LOOP2
JMP LOOP
LOOP2:
LDA $FE
STA $300,X
INX
CPX #0
BEQ LOOP3
JMP LOOP2
LOOP3:
LDA $FE
STA $400,X
INX
CPX #0
BEQ LOOP4
JMP LOOP3
LOOP4:
LDA $FE
STA #$500,X
INX
CPX #0
BEQ LOOP
JMP LOOP4
