.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[I from Label2 to Label3
	iconst_3
	iconst_4
	multianewarray [[I 2
	dup
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	dup
	iconst_0
	aaload
	iconst_2
	iconst_3
	iastore
	dup
	iconst_0
	aaload
	iconst_3
	iconst_4
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	bipush 6
	iastore
	dup
	iconst_1
	aaload
	iconst_2
	bipush 7
	iastore
	dup
	iconst_1
	aaload
	iconst_3
	bipush 8
	iastore
	dup
	iconst_2
	aaload
	iconst_0
	bipush 9
	iastore
	dup
	iconst_2
	aaload
	iconst_1
	bipush 10
	iastore
	dup
	iconst_2
	aaload
	iconst_2
	bipush 11
	iastore
	dup
	iconst_2
	aaload
	iconst_3
	bipush 12
	iastore
	astore_1
	aload_1
	iconst_1
	aaload
	iconst_2
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iconst_2
	aaload
	iconst_3
	iaload
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 55
.limit locals 2
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
