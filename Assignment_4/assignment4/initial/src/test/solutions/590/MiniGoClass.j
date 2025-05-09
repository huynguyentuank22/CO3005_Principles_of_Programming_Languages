.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a [I
.field static final b [F
.field static final c [LGoString;
.field static final d [LA;
.field static final e [[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a [I
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	getstatic MiniGoClass/b [F
	iconst_1
	faload
	invokestatic io/putFloat(F)V
	getstatic MiniGoClass/c [LGoString;
	iconst_0
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/d [LA;
	iconst_1
	aaload
	new GoString
	dup
	ldc "honors"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual A/main(LGoString;)V
	getstatic MiniGoClass/e [[I
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 9
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
	putstatic MiniGoClass/a [I
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
	putstatic MiniGoClass/b [F
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
	putstatic MiniGoClass/c [LGoString;
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
	putstatic MiniGoClass/d [LA;
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
	putstatic MiniGoClass/e [[I
Label0:
Label1:
	return
.limit stack 39
.limit locals 0
.end method
