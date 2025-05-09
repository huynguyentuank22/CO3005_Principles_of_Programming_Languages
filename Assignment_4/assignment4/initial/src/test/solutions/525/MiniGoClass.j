.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static b I

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
	invokestatic MiniGoClass/foo()V
	invokestatic MiniGoClass/bar()V
Label3:
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public static foo()V
Label0:
Label2:
	getstatic MiniGoClass/a I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static bar()V
Label0:
Label2:
	getstatic MiniGoClass/b I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
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
	iconst_1
	putstatic MiniGoClass/a I
	iconst_2
	putstatic MiniGoClass/b I
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
