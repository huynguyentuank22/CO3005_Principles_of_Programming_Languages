.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo()I
Label0:
Label2:
	bipush 28
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	invokestatic MiniGoClass/foo()I
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 1
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
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
