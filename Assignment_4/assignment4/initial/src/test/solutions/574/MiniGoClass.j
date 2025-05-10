.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I
.field static a [LString_MiniGo;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a1 [LString_MiniGo; from Label2 to Label3
	getstatic MiniGoClass/MAX I
	anewarray String_MiniGo
	dup
	iconst_0
	new String_MiniGo
	dup
	ldc "cc"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new String_MiniGo
	dup
	ldc "zz"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	astore_1
	getstatic MiniGoClass/a [LString_MiniGo;
	iconst_1
	aaload
	invokestatic MiniGoClass/foo(LString_MiniGo;)V
	aload_1
	iconst_0
	aaload
	invokestatic MiniGoClass/foo(LString_MiniGo;)V
	aload_1
	iconst_1
	aaload
	invokestatic MiniGoClass/foo(LString_MiniGo;)V
Label6:
.var 2 is i I from Label6 to Label7
	iconst_0
	istore_2
Label8:
	iload_2
	getstatic MiniGoClass/MAX I
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
Label12:
	getstatic MiniGoClass/a [LString_MiniGo;
	iload_2
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iload_2
	aaload
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label13:
	goto Label4
Label5:
Label7:
.var 3 is str LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "xx"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore_3
	aload_3
	invokestatic MiniGoClass/foo(LString_MiniGo;)V
	aload_3
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 15
.limit locals 4
.end method

.method public static foo(LString_MiniGo;)V
.var 0 is s LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	aload_0
	new String_MiniGo
	dup
	ldc "uu"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/compare(LString_MiniGo;)I
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	aload_0
	aload_0
	new String_MiniGo
	dup
	ldc "passbyref"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
Label10:
	goto Label7
Label6:
Label11:
Label12:
	aload_0
	new String_MiniGo
	dup
	ldc "pass"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
Label13:
Label7:
Label3:
Label1:
	return
.limit stack 10
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label14:
Label15:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	iconst_2
	putstatic MiniGoClass/MAX I
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
	putstatic MiniGoClass/a [LString_MiniGo;
Label0:
Label1:
	return
.limit stack 8
.limit locals 0
.end method
