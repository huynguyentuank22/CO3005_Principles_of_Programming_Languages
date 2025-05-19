.source Data.java
.class public Data
.super java.lang.Object
.field public val_int I
.field public val_float F

.method public <init>(IF)V
Label0:
.var 0 is this LData; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is val_int I from Label0 to Label1
.var 2 is val_float F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Data/val_int I
	aload_0
	fload_2
	putfield Data/val_float F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LData; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getInt()I
Label0:
.var 0 is this LData; from Label0 to Label1
Label2:
	aload_0
	getfield Data/val_int I
	getstatic MiniGoClass/offset_val I
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public getFloat()F
Label0:
.var 0 is this LData; from Label0 to Label1
Label2:
	aload_0
	getfield Data/val_float F
	getstatic MiniGoClass/offset_val I
	i2f
	fadd
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
