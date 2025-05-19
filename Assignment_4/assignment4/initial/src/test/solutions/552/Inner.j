.source Inner.java
.class public Inner
.super java.lang.Object
.field public val_y I

.method public <init>(I)V
Label0:
.var 0 is this LInner; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is val_y I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Inner/val_y I
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
Label0:
.var 0 is this LInner; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public show()V
Label0:
.var 0 is this LInner; from Label0 to Label1
Label2:
	aload_0
	getfield Inner/val_y I
	iconst_5
	iadd
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
