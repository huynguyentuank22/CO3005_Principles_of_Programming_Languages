.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is b I from Label2 to Label3
	bipush 10
	istore_2
.var 3 is c I from Label2 to Label3
	iload_1
	iload_2
	iadd
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
.var 4 is d I from Label2 to Label3
	iload_1
	iload_2
	isub
	istore 4
	iload 4
	invokestatic io/putIntLn(I)V
.var 5 is e I from Label2 to Label3
	iload_1
	iload_2
	imul
	istore 5
	iload 5
	invokestatic io/putIntLn(I)V
.var 6 is f I from Label2 to Label3
	iload_1
	iload_2
	idiv
	istore 6
	iload 6
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 7
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
