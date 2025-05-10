.source Score.java
.class public Score
.super java/lang/Object
.field points I

.method public <init>()V
.var 0 is this LScore; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public evaluate()LString_MiniGo;
.var 0 is this LScore; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Score/points I
	bipush 50
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	new String_MiniGo
	dup
	ldc "Pass"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	areturn
Label10:
Label6:
Label7:
	new String_MiniGo
	dup
	ldc "Fail"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	areturn
Label3:
Label1:
.limit stack 6
.limit locals 1
.end method
