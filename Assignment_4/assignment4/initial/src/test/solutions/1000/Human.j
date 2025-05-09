.source Human.java
.class public Human
.super java/lang/Object
.implements Speaker
.field name I

.method public <init>()V
.var 0 is this LHuman; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public speak()V
.var 0 is this LHuman; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Human/name I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
