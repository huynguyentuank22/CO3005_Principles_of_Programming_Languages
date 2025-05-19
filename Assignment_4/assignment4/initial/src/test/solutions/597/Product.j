.source Product.java
.class public Product
.super java.lang.Object
.field public id I
.field public price F

.method public <init>(IF)V
Label0:
.var 0 is this LProduct; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is id I from Label0 to Label1
.var 2 is price F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Product/id I
	aload_0
	fload_2
	putfield Product/price F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LProduct; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getIdPlusTen()I
Label0:
.var 0 is this LProduct; from Label0 to Label1
Label2:
	aload_0
	getfield Product/id I
	bipush 10
	iadd
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
