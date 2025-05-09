.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a F from Label2 to Label3
	ldc 5.0
	fstore_1
.var 2 is b F from Label2 to Label3
	fload_1
	ldc 5.6
	invokestatic MiniGoClass/foo(F)F
	fadd
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static foo(F)F
.var 0 is a F from Label0 to Label1
Label0:
Label2:
	fload_0
	ldc 5.0
	fadd
	freturn
Label3:
Label1:
.limit stack 2
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
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
