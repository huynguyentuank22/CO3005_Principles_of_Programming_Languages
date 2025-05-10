.source A.java
.class public A
.super java/lang/Object
.implements B
.field s LString_MiniGo;

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public setS(LString_MiniGo;)V
.var 0 is this LA; from Label0 to Label1
.var 1 is s LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	aload_0
 	getfield A/s LString_MiniGo;

	aload_1

	invokevirtual String_MiniGo/getValue()Ljava/lang/String;

	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V

Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public getS()LString_MiniGo;
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/s LString_MiniGo;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
