.source String_MiniGo.java
.class public String_MiniGo
.super java/lang/Object
.field private value Ljava/lang/String;


.method public <init>()V
.var 0 is this LString_MiniGo; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc ""
	putfield String_MiniGo/value Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>(Ljava/lang/String;)V
.var 0 is this LString_MiniGo; from Label0 to Label1
.var 1 is str Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield String_MiniGo/value Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public compare(LString_MiniGo;)I
.var 0 is this LString_MiniGo; from Label0 to Label1
.var 1 is other LString_MiniGo; from Label0 to Label1
Label0:
	aload_0
	getfield String_MiniGo/value Ljava/lang/String;
	aload_1
	getfield String_MiniGo/value Ljava/lang/String;
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public concat(LString_MiniGo;)LString_MiniGo;
.var 0 is this LString_MiniGo; from Label0 to Label1
.var 1 is other LString_MiniGo; from Label0 to Label1
Label0:
	new String_MiniGo
	dup
	aload_0
	getfield String_MiniGo/value Ljava/lang/String;
	aload_1
	getfield String_MiniGo/value Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	areturn
Label1:
.limit stack 4
.limit locals 2
.end method

.method public toString()Ljava/lang/String;
.var 0 is this LString_MiniGo; from Label0 to Label1
Label0:
	aload_0
	getfield String_MiniGo/value Ljava/lang/String;
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public getValue()Ljava/lang/String;
.var 0 is this LString_MiniGo; from Label0 to Label1
Label0:
	aload_0
	getfield String_MiniGo/value Ljava/lang/String;
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public setValue(Ljava/lang/String;)V
.var 0 is this LString_MiniGo; from Label0 to Label1
.var 1 is str Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	aload_1
	putfield String_MiniGo/value Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 2
.end method
