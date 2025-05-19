.source Node.java
.class public Node
.super java.lang.Object
.field public val_a I
.field public val_b F

.method public <init>(IF)V
Label0:
.var 0 is this LNode; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is val_a I from Label0 to Label1
.var 2 is val_b F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Node/val_a I
	aload_0
	fload_2
	putfield Node/val_b F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LNode; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public compute()I
Label0:
.var 0 is this LNode; from Label0 to Label1
Label2:
	aload_0
	getfield Node/val_a I
	iconst_5
	isub
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
