.source Coord.java
.class public Coord
.super java.lang.Object
.field public x_val I
.field public y_val F

.method public <init>(IF)V
Label0:
.var 0 is this LCoord; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is x_val I from Label0 to Label1
.var 2 is y_val F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Coord/x_val I
	aload_0
	fload_2
	putfield Coord/y_val F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LCoord; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getXTimesTen()I
Label0:
.var 0 is this LCoord; from Label0 to Label1
Label2:
	aload_0
	getfield Coord/x_val I
	bipush 10
	imul
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
