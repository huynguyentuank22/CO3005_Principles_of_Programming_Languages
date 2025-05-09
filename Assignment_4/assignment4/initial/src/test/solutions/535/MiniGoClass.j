.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a [I
.field static b [LA;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a [I
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	getstatic MiniGoClass/a [I
	iconst_1
	iaload
	invokestatic io/putInt(I)V
	getstatic MiniGoClass/a [I
	iconst_2
	iaload
	invokestatic io/putInt(I)V
	getstatic MiniGoClass/a [I
	iconst_3
	iaload
	invokestatic io/putInt(I)V
	getstatic MiniGoClass/a [I
	iconst_4
	iaload
	invokestatic io/putInt(I)V
	getstatic MiniGoClass/b [LA;
	iconst_0
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/b [LA;
	iconst_1
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/b [LA;
	iconst_2
	aaload
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 10
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
	putstatic MiniGoClass/a [I
	iconst_3
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
	putstatic MiniGoClass/b [LA;
Label0:
Label1:
	return
.limit stack 27
.limit locals 0
.end method
