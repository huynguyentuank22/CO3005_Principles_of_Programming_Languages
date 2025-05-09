.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is c F from Label2 to Label3
	getstatic MiniGoClass/a I
	i2f
	getstatic MiniGoClass/b F
	fadd
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 2
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
	iconst_0
	putstatic MiniGoClass/a I
	ldc 0.0
	putstatic MiniGoClass/b F
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
