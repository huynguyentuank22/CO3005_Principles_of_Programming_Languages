.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final M I
.field static final N I
.field static final P I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[[I from Label2 to Label3
	getstatic MiniGoClass/M I
	getstatic MiniGoClass/N I
	getstatic MiniGoClass/P I
	multianewarray [[[I 3
	dup
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_1
	bipush 6
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_1
	bipush 8
	iastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 44
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
	iconst_2
	putstatic MiniGoClass/M I
	iconst_2
	putstatic MiniGoClass/N I
	iconst_2
	putstatic MiniGoClass/P I
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
