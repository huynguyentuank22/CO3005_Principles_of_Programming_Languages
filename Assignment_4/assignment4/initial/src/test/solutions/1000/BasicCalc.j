.source BasicCalc.java
.class public BasicCalc
.super java/lang/Object
.implements Calculator
.field number I

.method public <init>()V
.var 0 is this LBasicCalc; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public calculate(II)V
.var 0 is this LBasicCalc; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
Label2:
	iload_1
	aload_0
	iadd
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method
