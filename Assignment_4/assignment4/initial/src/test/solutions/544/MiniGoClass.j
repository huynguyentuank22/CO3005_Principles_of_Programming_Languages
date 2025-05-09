.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.0
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	iconst_0
	faload
	invokestatic io/putFloatLn(F)V
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.0
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	iconst_1
	faload
	invokestatic io/putFloatLn(F)V
	iconst_2
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "World"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	iconst_0
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_2
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "World"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	iconst_1
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 36
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
