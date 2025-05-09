.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I

.method public static foo()V
Label0:
Label2:
.var 0 is a I from Label2 to Label3
	iconst_5
	istore_0
	iload_0
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	invokestatic MiniGoClass/foo()V
	getstatic MiniGoClass/a I
	invokestatic io/putInt(I)V
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
	bipush 10
	putstatic MiniGoClass/a I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
