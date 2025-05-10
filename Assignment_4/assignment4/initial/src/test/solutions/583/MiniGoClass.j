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
	dup
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	astore_1
	aload_1
	invokevirtual A/foo()LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual A/setS(LString_MiniGo;)V
	aload_1
	invokevirtual A/getS()LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 2 is b LB; from Label2 to Label3
	aload_1
	astore_2
	aload_2
	new String_MiniGo
	dup
	ldc "aaa"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokeinterface B/setS(LString_MiniGo;)V 2
	aload_2
	invokeinterface B/getS()LString_MiniGo; 1
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 3
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
