.source Box.java
.class public Box
.super java/lang/Object
.field width F
.field height F

.method public <init>()V
.var 0 is this LBox; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public area()F
.var 0 is this LBox; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Box/width F
	aload_0
	getfield Box/height F
	fmul
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
