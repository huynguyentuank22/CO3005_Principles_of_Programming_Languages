.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[F from Label2 to Label3
	getstatic MiniGoClass/MAX I
	getstatic MiniGoClass/MAX I
	multianewarray [[F 2
	astore_1
	getstatic MiniGoClass/MAX I
	getstatic MiniGoClass/MAX I
	multianewarray [[F 2
	dup
	iconst_0
	aaload
	iconst_0
	iconst_4
	i2f
	fastore
	dup
	iconst_0
	aaload
	iconst_1
	ldc 4.0
	fastore
	dup
	iconst_0
	aaload
	iconst_2
	iconst_4
	i2f
	fastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_4
	i2f
	fastore
	dup
	iconst_1
	aaload
	iconst_1
	ldc 4.0
	fastore
	dup
	iconst_1
	aaload
	iconst_2
	iconst_4
	i2f
	fastore
	dup
	iconst_2
	aaload
	iconst_0
	iconst_4
	i2f
	fastore
	dup
	iconst_2
	aaload
	iconst_1
	ldc 4.0
	fastore
	dup
	iconst_2
	aaload
	iconst_2
	iconst_4
	i2f
	fastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	faload
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 75
.limit locals 2
.end method

.method public static arrint(I)[I
.var 0 is val I from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/MAX I
	newarray int
	dup
	iconst_0
	iload_0
	iastore
	dup
	iconst_1
	iload_0
	iastore
	dup
	iconst_2
	iload_0
	iastore
	areturn
Label3:
Label1:
.limit stack 7
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
	iconst_3
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
