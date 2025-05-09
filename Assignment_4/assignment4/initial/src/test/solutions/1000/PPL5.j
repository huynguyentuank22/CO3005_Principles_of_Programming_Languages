.source PPL5.java
.class public PPL5
.super java/lang/Object
.implements Worker
.field number I

.method public <init>()V
.var 0 is this LPPL5; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public study()V
.var 0 is this LPPL5; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield PPL5/number I
	iconst_2
	imul
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
