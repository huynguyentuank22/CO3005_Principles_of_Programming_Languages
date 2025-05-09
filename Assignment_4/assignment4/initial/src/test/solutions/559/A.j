.source A.java
.class public A
.super java/lang/Object
.field x I
.field b LB;

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

.method public foo()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/x I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield A/b LB;
	invokevirtual B/foo()V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
