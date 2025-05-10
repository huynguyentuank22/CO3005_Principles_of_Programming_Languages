.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is x I from Label2 to Label3
	bipush 7
	istore_1
.var 2 is y I from Label2 to Label3
	iconst_3
	istore_2
.var 3 is z I from Label2 to Label3
	iload_1
	iload_2
	irem
	iload_1
	iload_2
	imul
	iadd
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 5
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
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
