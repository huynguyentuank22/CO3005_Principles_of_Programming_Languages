.source Product.java
.class public Product
.super java/lang/Object
.field price F
.field discount F

.method public <init>()V
.var 0 is this LProduct; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public finalPrice()F
.var 0 is this LProduct; from Label0 to Label1
Label0:
Label2:
.var 1 is discountAmount F from Label2 to Label3
	aload_0
	getfield Product/price F
	aload_0
	getfield Product/discount F
	fmul
	fstore_1
	aload_0
	getfield Product/price F
	fload_1
	fsub
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method
