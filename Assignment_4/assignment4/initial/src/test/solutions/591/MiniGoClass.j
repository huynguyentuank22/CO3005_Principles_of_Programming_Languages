.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [I from Label2 to Label3
	iconst_3
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
	astore_1
.var 2 is b [F from Label2 to Label3
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.5
	fastore
	dup
	iconst_1
	ldc 4.5
	fastore
	astore_2
.var 3 is c [LGoString; from Label2 to Label3
	iconst_2
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "hh"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "ll"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	astore_3
.var 4 is d [LA; from Label2 to Label3
	iconst_2
	anewarray A
	dup
	iconst_0
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_0
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	aastore
	dup
	iconst_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_0
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	aastore
	astore 4
.var 5 is e [[I from Label2 to Label3
	iconst_2
	iconst_2
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
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
	astore 5
.var 6 is f LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "aaa"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	astore 6
.var 7 is g LGoString; from Label2 to Label3
	aload 6
	new GoString
	dup
	ldc "hhh"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	astore 7
.var 8 is a1 I from Label2 to Label3
	iconst_1
	istore 8
.var 9 is b1 I from Label2 to Label3
	iconst_2
	iload 8
	bipush 7
	imul
	iadd
	istore 9
.var 10 is c1 I from Label2 to Label3
	iconst_3
	iload 9
	imul
	istore 10
.var 11 is d1 I from Label2 to Label3
	iconst_4
	iload 10
	imul
	istore 11
.var 12 is e1 F from Label2 to Label3
	ldc 5.0
	iload 10
	i2f
	fmul
	fstore 12
	aload_1
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	aload_2
	iconst_1
	faload
	invokestatic io/putFloat(F)V
	aload_3
	iconst_0
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload 4
	iconst_1
	aaload
	new GoString
	dup
	ldc "honors"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual A/main(LGoString;)V
	aload 5
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	aload 6
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload 7
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload 8
	invokestatic io/putIntLn(I)V
	iload 9
	invokestatic io/putIntLn(I)V
	iload 10
	invokestatic io/putIntLn(I)V
	iload 11
	invokestatic io/putIntLn(I)V
	fload 12
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 52
.limit locals 13
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
