.source Item.java
.class public Item
.super java.lang.Object
.field public val1 I
.field public val2 F

.method public <init>(IF)V
Label0:
.var 0 is this LItem; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is val1 I from Label0 to Label1
.var 2 is val2 F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Item/val1 I
	aload_0
	fload_2
	putfield Item/val2 F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LItem; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public process()I
Label0:
.var 0 is this LItem; from Label0 to Label1
Label2:
	aload_0
	getfield Item/val1 I
	iconst_1
	iadd
	iconst_2
	imul
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method
