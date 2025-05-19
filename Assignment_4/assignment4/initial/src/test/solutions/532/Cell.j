.source Cell.java
.class public Cell
.super java.lang.Object
.field public p I
.field public q F

.method public <init>(IF)V
Label0:
.var 0 is this LCell; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is p I from Label0 to Label1
.var 2 is q F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Cell/p I
	aload_0
	fload_2
	putfield Cell/q F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LCell; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public calc()I
Label0:
.var 0 is this LCell; from Label0 to Label1
Label2:
	aload_0
	getfield Cell/p I
	bipush 10
	iadd
	iconst_2
	idiv
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method
