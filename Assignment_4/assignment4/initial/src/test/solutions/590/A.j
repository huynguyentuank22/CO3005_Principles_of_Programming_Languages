.source A.java
.class public A
.super java/lang/Object
.field x I
.field y F

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

.method public main(LGoString;)V
.var 0 is this LA; from Label0 to Label1
.var 1 is s LGoString; from Label0 to Label1
Label0:
Label2:
	aload_1
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield A/x I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield A/y F
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 2
.end method
