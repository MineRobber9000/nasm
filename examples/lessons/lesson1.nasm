; Lesson 1 - Loading and Storing Data
; To load data into a register, use "load <register> <value>"
; Use cases:
; To load data into a register from a RAM address, i.e; "load a $fe"
; To load an immediate number into a register, i.e; "load x #0"
; To store data from a register use "store <register> <address>"
; Use cases:
; To store data from a register into a simple address, i.e; "store a $200"
; To store data from a register into an indexed address, i.e; "store a $200,x"
load a $fe
store a $200
