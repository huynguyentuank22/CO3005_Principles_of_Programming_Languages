.source Outer.java
.class public Outer
.super java.lang.Object
.field public val_x I
.field public inner_obj LInner;

.method public <init>(ILInner;)V
Label0:
.var 0 is this LOuter; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is val_x I from Label0 to Label1
.var 2 is inner_obj LInner; from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Outer/val_x I
	aload_0
	aload_2
	putfield Outer/inner_obj LInner;
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LOuter; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public display()V
Label0:
.var 0 is this LOuter; from Label0 to Label1
Label2:
	aload_0
	getfield Outer/val_x I
	iconst_2
	imul
	invokestatic io/putIntLn(I)V
	aload_0
	getfield Outer/inner_obj LInner;
	invokevirtual Inner/show()V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
