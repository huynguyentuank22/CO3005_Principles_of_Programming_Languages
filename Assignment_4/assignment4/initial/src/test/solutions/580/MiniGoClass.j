.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static arrStr(LString_MiniGo;)[LString_MiniGo;
.var 0 is v LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/MAX I
	anewarray String_MiniGo
	dup
	iconst_0
	new String_MiniGo
	dup
	ldc "abc"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new String_MiniGo
	dup
	ldc "xyz"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	areturn
Label3:
Label1:
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/arrStr(LString_MiniGo;)[LString_MiniGo;
	astore_1
	aload_1
	iconst_0
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 2 is b LString_MiniGo; from Label2 to Label3
	aload_1
	iconst_0
	aaload
	astore_2
	aload_1
	iconst_0
	new String_MiniGo
	dup
	ldc "def"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	aload_2
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
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
	iconst_2
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
