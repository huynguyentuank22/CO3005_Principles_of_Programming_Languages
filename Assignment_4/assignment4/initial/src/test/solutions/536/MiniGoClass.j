.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[LA; from Label2 to Label3
	iconst_2
	iconst_2
	multianewarray [[LA; 2
	dup
	iconst_0
	aaload
	iconst_0
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_1
	putfield A/x I
	dup
	ldc 2.0
	putfield A/y F
	aastore
	dup
	iconst_0
	aaload
	iconst_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_3
	putfield A/x I
	dup
	ldc 4.0
	putfield A/y F
	aastore
	dup
	iconst_1
	aaload
	iconst_0
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_5
	putfield A/x I
	dup
	ldc 6.0
	putfield A/y F
	aastore
	dup
	iconst_1
	aaload
	iconst_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	bipush 7
	putfield A/x I
	dup
	ldc 8.0
	putfield A/y F
	aastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
.var 2 is b [LA; from Label2 to Label3
	iconst_2
	anewarray A
	dup
	iconst_0
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_1
	putfield A/x I
	dup
	ldc 2.0
	putfield A/y F
	aastore
	dup
	iconst_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_3
	putfield A/x I
	dup
	ldc 4.0
	putfield A/y F
	aastore
	astore_2
	aload_2
	iconst_0
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 30
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
