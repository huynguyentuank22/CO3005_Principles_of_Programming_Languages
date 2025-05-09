.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I
.field static final b I
.field static final c I
.field static final d I
.field static final e F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/b I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/c I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/d I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/e F
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 1
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
	iconst_1
	putstatic MiniGoClass/a I
	iconst_2
	getstatic MiniGoClass/a I
	bipush 7
	imul
	iadd
	putstatic MiniGoClass/b I
	iconst_3
	getstatic MiniGoClass/b I
	imul
	putstatic MiniGoClass/c I
	iconst_4
	getstatic MiniGoClass/c I
	imul
	putstatic MiniGoClass/d I
	ldc 5.0
	getstatic MiniGoClass/c I
	i2f
	fmul
	putstatic MiniGoClass/e F
Label0:
Label1:
	return
.limit stack 7
.limit locals 0
.end method
