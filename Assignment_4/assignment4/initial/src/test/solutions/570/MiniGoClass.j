.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo()V
Label0:
Label2:
.var 0 is a LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "World"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore_0
	aload_0
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore_1
	aload_1
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic MiniGoClass/foo()V
	aload_1
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label4:
Label5:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
