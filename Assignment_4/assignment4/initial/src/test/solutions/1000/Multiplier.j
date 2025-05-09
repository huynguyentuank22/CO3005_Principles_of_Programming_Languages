.source Multiplier.java
.class public Multiplier
.super java/lang/Object
.field factor I

.method public <init>()V
.var 0 is this LMultiplier; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public multiply(I)I
.var 0 is this LMultiplier; from Label0 to Label1
.var 1 is value I from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Multiplier/factor I
	iload_1
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method
