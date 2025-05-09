.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final PI F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/PI F
	invokestatic io/putFloat(F)V
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
	ldc 3.14
	putstatic MiniGoClass/PI F
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
