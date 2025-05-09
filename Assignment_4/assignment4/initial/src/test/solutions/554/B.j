.source B.java
.class public B
.super java/lang/Object
.implements C
.field a I
.field b F

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
	bipush 10

	putfield B/a I
	aload_0
	ldc 20.0

	putfield B/b F
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public getA()I
.var 0 is this LB; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield B/a I
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
