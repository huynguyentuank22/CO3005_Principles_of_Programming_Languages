.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [LA;
.field static arr1 [LA;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_4
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
	dup
	iconst_2
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
	iconst_3
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
	putstatic MiniGoClass/arr [LA;
	getstatic MiniGoClass/arr [LA;
	iconst_0
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr [LA;
	iconst_1
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr [LA;
	iconst_2
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr [LA;
	iconst_3
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr1 [LA;
	iconst_0
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr1 [LA;
	iconst_1
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr1 [LA;
	iconst_2
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/arr1 [LA;
	iconst_3
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
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
	iconst_4
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
	dup
	iconst_2
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
	iconst_3
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
	putstatic MiniGoClass/arr1 [LA;
Label0:
Label1:
	return
.limit stack 15
.limit locals 0
.end method
