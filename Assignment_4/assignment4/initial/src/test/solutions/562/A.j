.source A.java
.class public A
.super java/lang/Object
.field x I
.field y F
.field z Z
.field s LGoString;

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public print()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/x I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield A/y F
	invokestatic io/putFloatLn(F)V
	aload_0
	getfield A/s LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield A/z Z
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
