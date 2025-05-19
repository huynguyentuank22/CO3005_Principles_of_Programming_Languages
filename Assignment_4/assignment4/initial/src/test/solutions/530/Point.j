.source Point.java
.class public Point
.super java.lang.Object
.field public a I
.field public b F

.method public <init>(IF)V
Label0:
.var 0 is this LPoint; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Point/a I
	aload_0
	fload_2
	putfield Point/b F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LPoint; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getA()I
Label0:
.var 0 is this LPoint; from Label0 to Label1
Label2:
	aload_0
	getfield Point/a I
	iconst_2
	imul
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
