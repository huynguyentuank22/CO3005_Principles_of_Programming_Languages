.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static getArr()[I
Label0:
Label2:
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	areturn
Label3:
Label1:
.limit stack 16
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[I from Label2 to Label3
	iconst_2
	iconst_5
	multianewarray [[I 2
	astore_1
	aload_1
	iconst_0
	invokestatic MiniGoClass/getArr()[I
	aastore
	aload_1
	iconst_1
	invokestatic MiniGoClass/getArr()[I
	aastore
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	aload_1
	iconst_1
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 9
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
