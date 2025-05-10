.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static test()LString_MiniGo;
Label0:
Label2:
.var 0 is a LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore_0
.var 1 is b LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "World"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore_1
.var 2 is c LString_MiniGo; from Label2 to Label3
	aload_0
	aload_1
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	astore_2
	aload_2
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static test1()LString_MiniGo;
Label0:
Label2:
	new String_MiniGo
	dup
	ldc "vibe coding"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 0
.end method

.method public static foo(LString_MiniGo;)V
.var 0 is s LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	aload_0
	aload_0
	new String_MiniGo
	dup
	ldc "lala"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
	aload_0
	aload_0
	new String_MiniGo
	dup
	ldc "meowmeow"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is str1 LString_MiniGo; from Label2 to Label3
	invokestatic MiniGoClass/test()LString_MiniGo;
	astore_1
	aload_1
	invokestatic MiniGoClass/foo(LString_MiniGo;)V
	aload_1
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
.var 2 is str2 LString_MiniGo; from Label2 to Label3
	invokestatic MiniGoClass/test1()LString_MiniGo;
	astore_2
	aload_2
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	invokestatic MiniGoClass/foo(LString_MiniGo;)V
	aload_2
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
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
