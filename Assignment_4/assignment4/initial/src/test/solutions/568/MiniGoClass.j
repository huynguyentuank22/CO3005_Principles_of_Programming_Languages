.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static fibo(I)I
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	iload_0
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	iload_0
	ireturn
Label10:
Label6:
Label7:
	iload_0
	iconst_1
	isub
	invokestatic MiniGoClass/fibo(I)I
	iload_0
	iconst_2
	isub
	invokestatic MiniGoClass/fibo(I)I
	iadd
	ireturn
Label3:
Label1:
.limit stack 8
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_3
	invokestatic MiniGoClass/fibo(I)I
	invokestatic io/putIntLn(I)V
	iconst_4
	invokestatic MiniGoClass/fibo(I)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 3
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
