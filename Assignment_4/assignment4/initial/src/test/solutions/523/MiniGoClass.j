.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LString_MiniGo;
.field static b LString_MiniGo;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	iconst_0
	istore_1
.var 2 is b I from Label2 to Label3
	iconst_0
	istore_2
	iconst_1
	iconst_2
	iadd
	istore_1
	iconst_3
	iconst_4
	isub
	istore_2
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 7
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
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/a LString_MiniGo;
	new String_MiniGo
	dup
	ldc "World"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/b LString_MiniGo;
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
