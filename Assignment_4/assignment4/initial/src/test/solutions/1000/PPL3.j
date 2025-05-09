.source PPL3.java
.class public PPL3
.super java/lang/Object
.implements PPL
.field a LPPL2;

.method public <init>()V
.var 0 is this LPPL3; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public returnPPL2()LPPL2;
.var 0 is this LPPL3; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield PPL3/a LPPL2;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
