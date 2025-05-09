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

.method public foo()I
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/x I
	iconst_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method

.method public bar()F
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/y F
	ldc 1.0
	fadd
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
