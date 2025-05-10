.source Library.java
.class public Library
.super java/lang/Object
.field name LString_MiniGo;
.field books [LString_MiniGo;

.method public <init>()V
.var 0 is this LLibrary; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public printBooks()V
.var 0 is this LLibrary; from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_0
	istore_1
Label8:
	iload_1
	iconst_3
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
	getfield Library/books [LString_MiniGo;
	iload_1
	aaload
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/compare(LString_MiniGo;)I
	ifeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label18:
Label19:
	new String_MiniGo
	dup
	ldc "- "
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aload_0
	getfield Library/books [LString_MiniGo;
	iload_1
	aaload
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label20:
Label16:
Label17:
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 12
.limit locals 2
.end method
