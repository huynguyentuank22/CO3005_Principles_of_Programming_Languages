.source Concrete.java
.class public Concrete
.super java.lang.Object
.implements Abstract
.field public num I

.method public <init>(I)V
Label0:
.var 0 is this LConcrete; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is num I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Concrete/num I
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
Label0:
.var 0 is this LConcrete; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getNum()I
Label0:
.var 0 is this LConcrete; from Label0 to Label1
Label2:
	aload_0
	getfield Concrete/num I
	iconst_1
	isub
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
