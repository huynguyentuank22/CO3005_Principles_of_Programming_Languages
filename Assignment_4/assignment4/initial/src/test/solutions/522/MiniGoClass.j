.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(IFZ)V
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c Z from Label0 to Label1
Label0:
Label2:
.var 3 is a F from Label2 to Label3
	ldc 0.0
	fstore_3
.var 4 is b I from Label2 to Label3
	iconst_0
	istore 4
.var 5 is c LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore 5
	ldc 5.0
	fstore_3
	bipush 10
	istore 4
	aload 5
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
	fload_3
	invokestatic io/putFloatLn(F)V
	iload 4
	invokestatic io/putIntLn(I)V
	aload 5
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 6
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_5
	ldc 10.0
	iconst_1
	invokestatic MiniGoClass/foo(IFZ)V
Label3:
Label1:
	return
.limit stack 4
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
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
