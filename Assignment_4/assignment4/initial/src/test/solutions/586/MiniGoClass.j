.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static e I
.field static d LString_MiniGo;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	astore_1
.var 2 is b I from Label2 to Label3
	iconst_0
	istore_2
.var 3 is c Z from Label2 to Label3
	iconst_0
	istore_3
.var 4 is d F from Label2 to Label3
	ldc 0.0
	fstore 4
Label3:
Label1:
	return
.limit stack 3
.limit locals 5
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
	iconst_0
	putstatic MiniGoClass/e I
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/d LString_MiniGo;
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
