.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static k I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_1
	putfield A/x I
	dup
	ldc 2.0
	putfield A/y F
	invokevirtual A/foo()I
	invokestatic io/putInt(I)V
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_3
	putfield A/x I
	dup
	ldc 4.0
	putfield A/y F
	invokevirtual A/bar()F
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 5
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
	putstatic MiniGoClass/k I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
