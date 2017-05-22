; Program to fill the screen with random colors
; By MineRobber9000
load x #0 ; Initialize X
Loop:
load a $fe ; Get random number (6502asm.com exclusive)
store a $200,x ; Store in VRAM
inc x ; Increment X to move up a pixel
compare x #0 ; Has X overflown?
branch equal Loop2 ; If so, jump to next loop
branch unconditional Loop ; Otherwise, start over from the top of the Loop (same instructions down to the 
;                           bottom with increased memory locations)
Loop2:
load a $fe
store a $300,x
inc x
compare x #0
branch equal Loop3
branch unconditional Loop2
Loop3:
load a $fe
store a $400,x
inc x
compare x #0
branch equal Loop4
branch unconditional Loop3
Loop4:
load a $fe
store a #$500,x
inc x
compare x #0
branch equal Loop ; If X overflows in loop 4, go back to first loop
branch unconditional Loop4
