.source A.java
.class public A
.super java/lang/Object
.implements B
.field _s [LString_MiniGo;

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

.method public setS([LString_MiniGo;)V
.var 0 is this LA; from Label0 to Label1
.var 1 is s [LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	aload_0
	aload_1

	putfield A/_s [LString_MiniGo;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public getS()[LString_MiniGo;
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/_s [LString_MiniGo;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method

.method public printS()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_0
	istore_1
Label8:
	iload_1
	iconst_5
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label12:
	aload_0
	getfield A/_s [LString_MiniGo;
	iload_1
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 8
.limit locals 2
.end method
