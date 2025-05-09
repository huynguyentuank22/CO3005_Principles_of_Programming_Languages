.source B.java
.class public B
.super java/lang/Object
.field y I

.method public <init>()V
.var 0 is this LB; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public foo()V
.var 0 is this LB; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield B/y I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
