.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	astore_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_5
	putfield A/x I
	dup
	ldc 10.0
	putfield A/y F
	astore_1
	aload_1
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
	aload_1
	invokevirtual A/bar()F
	invokestatic io/putFloatLn(F)V
.var 2 is b LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	bipush 10
	putfield A/x I
	dup
	ldc 20.0
	putfield A/y F
	astore_2
	aload_2
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
.var 3 is c LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	bipush 10
	putfield A/x I
	dup
	ldc 8.5
	putfield A/y F
	astore_3
	aload_3
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 4
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
