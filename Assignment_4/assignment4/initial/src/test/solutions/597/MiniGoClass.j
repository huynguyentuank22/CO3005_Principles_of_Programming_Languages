.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is fleet [LTransport; from Label2 to Label3
	iconst_2
	anewarray Transport
	dup
	iconst_0
	new Vehicle
	dup
	invokespecial Vehicle/<init>()V
	dup
	bipush 60
	putfield Vehicle/speed I
	aastore
	dup
	iconst_1
	new Vehicle
	dup
	invokespecial Vehicle/<init>()V
	dup
	bipush 80
	putfield Vehicle/speed I
	aastore
	astore_1
.var 2 is total I from Label2 to Label3
	aload_1
	iconst_0
	aaload
	invokeinterface Transport/getSpeed()I 1
	aload_1
	iconst_1
	aaload
	invokeinterface Transport/getSpeed()I 1
	iadd
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 11
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
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
