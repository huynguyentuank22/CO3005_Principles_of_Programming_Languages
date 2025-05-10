.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static genStr(LString_MiniGo;)LString_MiniGo;
.var 0 is v LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	aload_0
	new String_MiniGo
	dup
	ldc "aa"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	new String_MiniGo
	dup
	ldc "bc"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	areturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [LString_MiniGo; from Label2 to Label3
	getstatic MiniGoClass/MAX I
	anewarray String_MiniGo
	dup
	iconst_0
	new String_MiniGo
	dup
	ldc "pp"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new String_MiniGo
	dup
	ldc "cc"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	astore_1
.var 2 is b LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "jj"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/genStr(LString_MiniGo;)LString_MiniGo;
	astore_2
.var 3 is c LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "ii"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/genStr(LString_MiniGo;)LString_MiniGo;
	astore_3
Label3:
Label1:
	return
.limit stack 7
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
	iconst_2
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
