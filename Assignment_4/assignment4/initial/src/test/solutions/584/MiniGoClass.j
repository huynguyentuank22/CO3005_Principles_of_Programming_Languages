.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static complex(LA;[LString_MiniGo;LB;)V
.var 0 is a LA; from Label0 to Label1
.var 1 is arr [LString_MiniGo; from Label0 to Label1
.var 2 is b LB; from Label0 to Label1
Label0:
Label2:
	aload_0
	invokevirtual A/getS()LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	invokeinterface B/getS()LString_MiniGo; 1
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	new A
	dup
	invokespecial A/<init>()V
	dup
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	getstatic MiniGoClass/MAX I
	anewarray String_MiniGo
	dup
	iconst_0
	new String_MiniGo
	dup
	ldc "aa"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new String_MiniGo
	dup
	ldc "bb"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	new A
	dup
	invokespecial A/<init>()V
	dup
	new String_MiniGo
	dup
	ldc "uu"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	invokestatic MiniGoClass/complex(LA;[LString_MiniGo;LB;)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 1
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
