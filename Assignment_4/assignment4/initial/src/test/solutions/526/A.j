.source A.java
.class public A
.super java/lang/Object
.implements B
.implements C
.field a I
.field b F

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
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
