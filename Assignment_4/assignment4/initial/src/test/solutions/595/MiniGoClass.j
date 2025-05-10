.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is box LBox; from Label2 to Label3
	new Box
	dup
	invokespecial Box/<init>()V
	dup
	ldc 4.5
	putfield Box/width F
	dup
	ldc 2.0
	putfield Box/height F
	astore_1
	aload_1
	invokevirtual Box/area()F
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 3
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
