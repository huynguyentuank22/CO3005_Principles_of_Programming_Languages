.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	astore_1
.var 2 is b LB; from Label2 to Label3
	aload_1
	astore_2
.var 3 is c [LString_MiniGo; from Label2 to Label3
	iconst_5
	anewarray String_MiniGo
	dup
	iconst_0
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new String_MiniGo
	dup
	ldc "World"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_2
	new String_MiniGo
	dup
	ldc "!"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_3
	new String_MiniGo
	dup
	ldc "This"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_4
	new String_MiniGo
	dup
	ldc "is"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	astore_3
	aload_2
	aload_3
	invokeinterface B/setS([LString_MiniGo;)V 2
	aload_2
	invokeinterface B/getS()[LString_MiniGo; 1
	iconst_0
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokeinterface B/getS()[LString_MiniGo; 1
	iconst_1
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokeinterface B/getS()[LString_MiniGo; 1
	iconst_2
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 16
.limit locals 4
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
